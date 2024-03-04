from flask_restful import Resource, reqparse
from flask import make_response, render_template
from app.models.user import User

#Recuperando valores do formulario
data = reqparse.RequestParser()
data.add_argument("nome", type=str, help="Nome do usuario", required=True, location="form")
data.add_argument("sobrenome", type=str, help="Sobrenome do usuário",location="form")
data.add_argument("email", type=str, help="Email cadastrado para login do usuario", required=True, location="form")
data.add_argument("senha", type=str, help="Senha cadastrada do usuario", required=True, location="form")
class Cadastro(Resource):
  def get(self):
    headers = {"Content-Type": "text/html"}
    return make_response(render_template("cadastro.html"), 200, headers)
  
  def post(self):
    args = data.parse_args()
    
    try:
      cadastro = User(nome=args['nome'], 
                      sobrenome=args['sobrenome'], 
                      email=args['email'],
                      senha=args['senha'])
      cadastro.save()
      return f"Usuario criado com sucesso! {cadastro}", 201
    
    except Exception as e:
      return f"Error: {e}",401