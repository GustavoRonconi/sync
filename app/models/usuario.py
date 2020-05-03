from app.database import db
from passlib.apps import custom_app_context as pwd_context


class Usuario(db.Model):
    __tablename__ = "usuario"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    id_pessoa = db.Column(db.Integer, db.ForeignKey("pessoa.id"), nullable=False)
    hash_senha = db.Column(db.String(200))

    def __init__(self, email=None, id_pessoa=None):
        self.email = email
        self.id_pessoa = id_pessoa

    def fazer_hash_senha(self, senha):
        """Método utilizado para encriptar senha antes de salvar"""
        self.hash_senha = pwd_context.encrypt(senha)

    def verificar_senha(self, senha):
        """Método utilizado para a verificação de senha"""
        return pwd_context.verify(senha, self.hash_senha)

    @property
    def serialize(self):
        """Retorna o objeto serializado"""
        return {"id": self.id, "email": self.email}
