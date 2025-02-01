from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__, template_folder="templates")

    from routes import rutas
    rutas(app)
    
    return app