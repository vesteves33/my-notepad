from flask_restful import Resource
from flask import make_response, render_template

class Home(Resource):
  def get(self):
    headers = {"Content-Type": "text/html"}
    return make_response(render_template('home.html'), 200, headers)
