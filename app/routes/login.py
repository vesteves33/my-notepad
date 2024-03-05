from flask_restful import Resource, reqparse
from flask import make_response, render_template, flash, redirect, url_for
from app import bcrypt
from app.models.user import User

parser = reqparse.RequestParser()
parser.add_argument("email", type=str, required=True, location='form')
parser.add_argument("senha", type=str, required=True, location='form')

class Login(Resource):
  def get(self):
    headers = {"Content-Type": "text/html"}
    return make_response(render_template("login.html"), 200, headers)
  
  def post(self):
    args = parser.parse_args()

    try:
      usuario = User.query.filter_by(email=args['email']).first()

      if usuario and bcrypt.check_password_hash(usuario.senha, args['senha']):
        flash("Logado!","alert-success")
        return redirect(url_for('login'))
    
    except Exception as e:
      return f"Error: {e}"
    

