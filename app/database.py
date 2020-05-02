from flask_sqlalchemy import SQLAlchemy
import configparser
from app import app

"""Importa a configuração da aplicação"""
configuration = configparser.RawConfigParser()
configuration.read("./application.config")


DATA_BASE_URI = configuration.get("DATABASE", "DATABASE_URI")


app.config["SQLALCHEMY_DATABASE_URI"] = DATA_BASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
