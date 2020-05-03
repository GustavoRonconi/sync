from app.models import Pessoa
from app.models import Usuario
from app.database import db
from flask import Response, jsonify
import json
from flask_jwt_extended import create_access_token, create_refresh_token


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


def users_record(user_id=None):
    try:
        if user_id:
            query = db.session.query(Usuario).filter(Usuario.id == user_id).first()
            return jsonify(query.serialize)
        query = db.session.query(Usuario).all()
        return jsonify([i.serialize for i in query])
    except Exception:
        return Response(
            json.dumps({"errors": "Internal Server Error"}),
            status=500,
            mimetype="application/json",
        )


def auth_login(valid_payload):
    unauthorized = Response(
        json.dumps({"errors": "Não autorizado"}),
        status=401,
        mimetype="application/json",
    )

    try:
        user = (
            db.session.query(Usuario)
            .filter(Usuario.email == valid_payload["email"])
            .first()
        )
        if user:
            verify_password = user.verificar_senha(valid_payload["senha"])
            if verify_password:
                return Response(
                    json.dumps(
                        {
                            "token": create_access_token(identity=user.email),
                            "refresh_token": create_refresh_token(identity=user.email),
                        }
                    ),
                    status=200,
                    mimetype="application/json",
                )
        return unauthorized

    except Exception:
        return Response(
            json.dumps({"errors": "Internal Server Error"}),
            status=500,
            mimetype="application/json",
        )
