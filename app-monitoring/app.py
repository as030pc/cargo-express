from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from models import db, User, Pedido, Repartidor, Producto
import datetime

app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

# Rutas de Autenticación
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']
    user = User.query.filter_by(username=username, password=password).first()
    if user:
        access_token = create_access_token(identity={'username': user.username})
        return jsonify(access_token=access_token), 200
    return jsonify(message="Invalid credentials"), 401

# Métrica: Cantidad de entregas por hora por repartidor
@app.route('/api/metrics/deliveries_per_hour', methods=['GET'])
@jwt_required()
def deliveries_per_hour():
    now = datetime.datetime.now()
    one_hour_ago = now - datetime.timedelta(hours=1)
    results = db.session.query(Repartidor.nombre, db.func.count(Pedido.id)).\
        join(Pedido, Repartidor.id == Pedido.repartidor_id).\
        filter(Pedido.fecha_entrega >= one_hour_ago).\
        group_by(Repartidor.nombre).all()
    return jsonify(results)

# Métrica: Productos más vendidos
@app.route('/api/metrics/top_products', methods=['GET'])
@jwt_required()
def top_products():
    results = db.session.query(Producto.nombre, db.func.count(Pedido.id)).\
        join(Pedido, Producto.id == Pedido.id).\
        group_by(Producto.nombre).\
        order_by(db.func.count(Pedido.id).desc()).all()
    return jsonify(results)

# Métrica: Tiempo promedio de entrega por repartidor
@app.route('/api/metrics/average_delivery_time', methods=['GET'])
@jwt_required()
def average_delivery_time():
    now = datetime.datetime.now()
    one_month_ago = now - datetime.timedelta(days=30)
    
    results = db.session.query(
        Repartidor.nombre,
        db.func.avg(Pedido.fecha_entrega - Pedido.fecha_registro).label('average_delivery_time')
    ).join(Pedido, Repartidor.id == Pedido.repartidor_id).filter(Pedido.fecha_entrega >= one_month_ago).group_by(Repartidor.nombre).all()

    formatted_results = [
        {
            'repartidor': r.nombre,
            'average_delivery_time_seconds': r.average_delivery_time.total_seconds()
        } for r in results
    ]
    
    return jsonify(formatted_results)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)