from flask_restful import Resource
from flask import make_response, render_template

class Register(Resource):
  def get(self):
    headers = {"Content-Type": "text/html"}
    return make_response(render_template("register.html"), 200, headers)