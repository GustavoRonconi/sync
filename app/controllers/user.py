from app.models import Pessoa
from app.models import Usuario
from app.database import db
from flask import Response
import json


def create_user_record(valid_payload):
    try:
        pessoa = Pessoa(valid_payload["nome"], valid_payload["data_nascimento"])
        db.session.add(pessoa)
        db.session.flush()
        usuario = Usuario(valid_payload["email"], pessoa.id)
        usuario.fazer_hash_senha(valid_payload["senha"])
        db.session.add(usuario)
        db.session.commit()
        return Response(
            json.dumps(valid_payload), status=201, mimetype="application/json",
        )
    except Exception:
        return Response(
            json.dumps({"errors": "Internal Server Error"}),
            status=500,
            mimetype="application/json",
        )
