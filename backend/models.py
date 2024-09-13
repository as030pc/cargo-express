

from app import db

class Producto(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.String(10), primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)

class Repartidor(db.Model):
    __tablename__ = 'repartidores'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

class Pedido(db.Model):
    __tablename__ = 'pedidos'
    id = db.Column(db.String(36), primary_key=True)
    repartidor_id = db.Column(db.Integer, db.ForeignKey('repartidores.id'), nullable=False)
    fecha_entrega = db.Column(db.DateTime, nullable=False)

    repartidor = db.relationship('Repartidor', back_populates='pedidos')
    productos = db.relationship('DetallePedido', back_populates='pedido')

class DetallePedido(db.Model):
    __tablename__ = 'detalle_pedido'
    pedido_id = db.Column(db.String(36), db.ForeignKey('pedidos.id'), primary_key=True)
    producto_id = db.Column(db.String(10), db.ForeignKey('productos.id'), primary_key=True)
    cantidad = db.Column(db.Integer, nullable=False)

    pedido = db.relationship('Pedido', back_populates='productos')
    producto = db.relationship('Producto', back_populates='pedidos')