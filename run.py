#Import das dependencias do projeto
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api

#Import das Rotas
from app.routes.home import Home
from app.routes.cadastro import Cadastro
from app.routes.login import Login

app = Flask(__name__, template_folder="app/templates")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/vitor/Documentos/codigos/python/my-notepad/mynotepad.db'

db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)

api.add_resource(Home, "/")
api.add_resource(Cadastro, "/register")
api.add_resource(Login, "/login")

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0")