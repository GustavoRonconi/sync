from app.validators import GenericValidator
from flask import Response
import json


class UserCreateValidator(GenericValidator):
    """Classe de validação específica da rotina de criação de usuários"""
    def __init__(self, required_fields, dict_fields, unique_fields):
        super().__init__(required_fields, dict_fields, unique_fields)

    def minimun_password(self):
        """Verifica se o password possuir uma quantidade mínima de caracteres"""
        if len(self.dict_fields["senha"]) < 8:
            return Response(
                json.dumps({"errors": "A senha deve possuir no mínimo 8 caracteres!"}),
                status=422,
                mimetype="application/json",
            )
