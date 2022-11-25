from flask import request
from flask_restful import Resource
from services.auth import AuthenticationService
from services.otp import OtpService

from utils.check_fields import check_fields

class Authentication(Resource):

    @check_fields(fields=["email", "password"])
    def post(self, service):
        data: dict = request.json
        if service=="register":
            return AuthenticationService.register_user(**data)
        elif service=="login":
            return AuthenticationService.login_user(**data)
        raise Exception("Invalid Service", 401)