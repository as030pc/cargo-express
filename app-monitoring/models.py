from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

class Producto(db.Model):
    id = db.Column(db.String(10), primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)

class Repartidor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    pedidos = db.relationship('Pedido', backref='repartidor', lazy=True)

class Pedido(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    repartidor_id = db.Column(db.Integer, db.ForeignKey('repartidor.id'), nullable=False)
    fecha_registro = db.Column(db.DateTime, nullable=False)
    fecha_entrega = db.Column(db.DateTime, nullable=False)