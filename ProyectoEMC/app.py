from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    # SERVER LOCAL FKN
    # user    = "admin"
    # pswd    = "admin"  
    # srv     = "(localdb)\\ServidorDB"
    # db      = "dbfool"
    
    # SERVER MADRID
    user    = "sa"
    pswd    = "P%40ssw0rd"  
    srv     = "26.145.122.242\\MSSQLSERVERENTER"
    dbase   = "MADRID_EMC"
    
    # SERVER BARCELONA
    # user    = "sa"
    # pswd    = "P%40ssw0rd"  
    # srv     = "26.145.122.242\\MSSQLSERVERENTER"
    # db      = "MADRID_EMC"
    
    app = Flask(__name__, template_folder="templates")
    
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mssql+pyodbc://{user}:{pswd}@{srv}/{dbase}?driver=ODBC+Driver+17+for+SQL+Server'    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from routes import rutas
    rutas(app, db)
    # migrate = Migrate(app, db)
    
    return app