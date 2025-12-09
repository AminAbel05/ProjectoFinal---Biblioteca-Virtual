from flask import Flask
from .database import init_db

def crear_web():
    app = Flask(__name__)
    app.secret_key = "clave_secreta"

    init_db()

    from .routes import main
    app.register_blueprint(main)

    return app