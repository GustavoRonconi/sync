import json

from flask import Response, request
from flask_jwt_extended import (
    get_jwt_identity,
    jwt_refresh_token_required,
    jwt_required,
    create_access_token,
)

from app import app
from app.controllers import auth_login, create_user_record, users_record
from app.models import Usuario
from app.validators import GenericValidator, UserCreateValidator


@app.route("/criar_usuario", methods=["POST"])
@jwt_required
def create_user():
    """Cria um Usuario"""
    required_fields = ["nome", "data_nascimento", "email", "senha"]
    unique_fields = {"email": Usuario.email}
    dict_fields = UserCreateValidator.make_dict(request.data)
    if type(dict_fields) is not dict:
        return dict_fields
    validator = UserCreateValidator(required_fields, dict_fields, unique_fields)
    if validator.execute_all_validators():
        return validator.execute_all_validators()
    return create_user_record(dict_fields)


@app.route("/usuarios", methods=["GET"])
@jwt_required
def get_usuarios():
    """Todos os usuarios"""
    return users_record()


@app.route("/usuarios/<int:user_id>", methods=["GET"])
@jwt_required
def get_usuario(user_id):
    """Um usuario"""
    return users_record(user_id)


@app.route("/login", methods=["POST"])
def login():
    """Autentica no sistema"""
    required_fields = ["email", "senha"]
    dict_fields = GenericValidator.make_dict(request.data)
    if type(dict_fields) is not dict:
        return dict_fields
    validator = GenericValidator(required_fields, dict_fields, {})
    if validator.execute_all_validators():
        return validator.execute_all_validators()
    return auth_login(dict_fields)


@app.route("/refresh_token", methods=["POST"])
@jwt_refresh_token_required
def refresh():
    """Atualiza a sessão"""
    current_user = get_jwt_identity()
    return Response(
        json.dumps({"token": create_access_token(identity=current_user)}),
        status=200,
        mimetype="application/json",
    )
