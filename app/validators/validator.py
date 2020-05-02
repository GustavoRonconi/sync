from flask import Response
import json
from app.database import db


class Validator:
    def __init__(self, required_fields, dict_fields, unique_fields):
        self.required_fields = sorted(required_fields)
        self.dict_fields = dict_fields
        self.list_fields = sorted(self.dict_fields.keys())
        self.unique_fields = unique_fields

    @staticmethod
    def make_dict(payload):
        """Retorna o dicionário ou um erro"""
        try:
            return json.loads(payload)
        except Exception:
            return Response(
                json.dumps({"errors": "Bad Request!"}),
                status=400,
                mimetype="application/json",
            )

    def check_validator(self) -> Response:
        """Checa se a payload possui todos os dados necessários"""
        if self.list_fields != self.required_fields:
            return Response(
                json.dumps({"errors": "Parâmetros inválidos!"}),
                status=422,
                mimetype="application/json",
            )

    def duplicate_unique_fields(self) -> Response:
        """Verifica se existe entradas duplicadas no modelo"""
        for field, model_value in self.unique_fields.items():
            duplicate = db.session.query(
                db.exists().where(model_value == self.dict_fields[field])
            ).scalar()
            if duplicate:
                return Response(
                    json.dumps(
                        {"errors": f"Registro duplicado: {self.dict_fields[field]}"}
                    ),
                    status=422,
                    mimetype="application/json",
                )

    def execute_all_validators(self) -> Response:
        """Executa todos os métodos de validação"""
        for i in dir(self):
            method = getattr(self, i)
            conditions = (
                callable(method)
                and i not in ["execute_all_validators", "make_dict"]
                and "__" not in i
            )
            if conditions:
                call = method()
                if call:
                    return method()
