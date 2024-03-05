#Import das dependencias do projeto
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_bcrypt import Bcrypt

app = Flask(__name__, template_folder="templates")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mynotepad.db'
app.config['SECRET_KEY'] = '386d859545e57f7bf41cb5abc1ed8af68bb715ec5529b42fb3063ad1931eb959'

db = SQLAlchemy(app)
api = Api(app)
bcrypt = Bcrypt(app)

#Import das Rotas
from app.routes.home import Home
from app.routes.cadastro import Cadastro
from app.routes.login import Login

api.add_resource(Home, "/")
api.add_resource(Cadastro, "/cadastro")
api.add_resource(Login, "/login")

#Import das Models
from app.models import user, note

#Criação do database e das tabelas
with app.app_context():
  db.create_all()





