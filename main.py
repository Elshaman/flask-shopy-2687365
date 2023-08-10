from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
from datetime import datetime

#creacion y configuracion de la app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:@localhost/flask-shopy-2687365'
#crear los objetos de SQLalchemy y migrate
db = SQLAlchemy(app)
migrate = Migrate(app ,
                  db)

#modelos
class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100) , unique = True)
    email = db.Column(db.String(120) , unique = True)
    password = db.Column(db.String(128) )


class Producto(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100))
    precio = db.Column(db.Numeric(precision = 10 , scale = 2))
    imagen = db.Column(db.String(100))

class Venta(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    fecha = db.Column(db.DateTime , default = datetime.utcnow)
    cliente_id = db.Column(db.Integer , db.ForeignKey('cliente.id'))