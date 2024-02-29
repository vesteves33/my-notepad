from flask import Flask
from flask_restful import Api
from app.routes.home import Home
from app.routes.register import Register

app = Flask(__name__, template_folder="app/templates")
api = Api(app)

api.add_resource(Home, "/")
api.add_resource(Register, "/register")



if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0")