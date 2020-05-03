from flask import Flask
from flask_jwt_extended import JWTManager


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "Inject!on.777"  # TODO colocar no application.config
app.config["JWT_ERROR_MESSAGE_KEY"] = "errors"
jwt = JWTManager(app)

from app import routes

routes_list = [routes]