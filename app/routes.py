from app.validators import UserCreateValidator
from flask import request
from app.controllers import create_user_record
from app import app
from app.models import Usuario


@app.route("/criar_usuario", methods=["GET", "POST"])
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
