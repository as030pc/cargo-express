
from routes.pedidos import pedidos_bp

def init_routes(app):
    app.register_blueprint(pedidos_bp)