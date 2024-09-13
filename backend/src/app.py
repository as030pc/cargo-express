from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

# Inicialización de la app
app = Flask(__name__)
app.config.from_object(Config)

# Inicialización de la base de datos
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Registrar las rutas
from routes import init_routes
init_routes(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)