from sqlalchemy import Column, Integer, String
from connection import Base


class Usuario(Base):
    __tablename__ = "Usuario"
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    email = Column(String(120), unique=True)
    senha = Column(String(200))

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email
