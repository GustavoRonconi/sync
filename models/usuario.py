from database import db


class Usuario(db.Model):
    __tablename__ = "Usuario"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True)
    senha = db.Column(db.String(200))

    def __init__(self, name=None, email=None, senha=None):
        self.name = name
        self.email = email
        self.senha = senha
