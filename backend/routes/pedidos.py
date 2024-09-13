from flask import Blueprint, jsonify, request
from models import Pedido
import datetime
from app import db

pedidos_bp = Blueprint('pedidos', __name__)

@pedidos_bp.route('/api/pedidos', methods=['POST'])
def create_pedido():
    data = request.json
    fecha_entrega = datetime.datetime.strptime(data['fecha_entrega'], '%Y-%m-%d %H:%M:%S')
    ahora = datetime.datetime.now()
    diferencia_tiempo = ahora - fecha_entrega

    if diferencia_tiempo.total_seconds() > 10:
        return jsonify({'error': 'La entrega excede el límite de 10 segundos para ser registrada.'}), 400

    nuevo_pedido = Pedido(
        id=data['id'],
        repartidor_id=data['repartidor_id'],
        fecha_entrega=fecha_entrega
    )
    
    db.session.add(nuevo_pedido)
    db.session.commit()
    return jsonify({'message': 'Pedido creado exitosamente'}), 201