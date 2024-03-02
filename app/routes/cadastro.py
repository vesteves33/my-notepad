from flask_restful import Resource
from flask import make_response, render_template

class Cadastro(Resource):
  def get(self):
    headers = {"Content-Type": "text/html"}
    return make_response(render_template("cadastro.html"), 200, headers)
  
  def post(self):
    pass

