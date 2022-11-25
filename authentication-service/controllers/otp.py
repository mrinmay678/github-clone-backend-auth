from flask import request
from flask_restful import Resource
from services.otp import OtpService

from utils.check_fields import check_fields

class OTP(Resource):

    @check_fields(fields=["otp", "email"])
    def post(self):
        data: dict = request.json
        OtpService.check_otp(**data)

    @check_fields(fields=["email"])
    def get(self):
        data: dict = request.json
        OtpService.send_otp(**data)

