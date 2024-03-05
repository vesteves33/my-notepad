from flask_restful import Resource, reqparse
from flask import make_response, render_template, redirect, flash, url_for
from app.models.user import User
from app import bcrypt

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
    senha = bcrypt.generate_password_hash(args["senha"], 12)
    
    try:
      cadastro = User(nome=args['nome'], 
                      sobrenome=args['sobrenome'], 
                      email=args['email'],
                      senha=senha)
      cadastro.save()
      
      flash(f"Usuario {cadastro} criado com sucesso!", "alert-success")
      return redirect(url_for('cadastro'))
    
    except Exception as e:
      return f"Error: {e}",401