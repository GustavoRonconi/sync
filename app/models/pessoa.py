from app.database import db


class Pessoa(db.Model):
    __tablename__ = "pessoa"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    data_nascimento = db.Column(db.Date)

    def __init__(self, nome=None, data_nascimento=None):
        self.nome = nome
        self.data_nascimento = data_nascimento

    usuarios = db.relationship("Usuario", backref="pessoa", lazy=True)
