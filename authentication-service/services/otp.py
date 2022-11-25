from datetime import datetime
import math
import random
from models import otp_manager
from models.otp_manager import OtpManagerDocument
from models.user import UserDocument
from tasks import send_otp_via_email, send_otp_via_phone
from mongoengine.errors import DoesNotExist

class OtpService:

    # Creating OTP
    def _generate(self):
        digits: str = "0123456789"
        otp: list = []
        for _ in range(6):
            otp.append(digits[math.floor(random.random() * 10)])
        otp = "".join(otp)
        return otp

    @classmethod
    def otp_generator(cls, email):
        try:
            otp_obj = OtpManagerDocument.objects.get(email=email)
            if datetime.now() < otp_obj.expiry:
                otp = otp_obj.otp
            else:
                otp_obj.otp = otp = cls._generate()
                otp_obj.save()

        except DoesNotExist:
            obj = OtpManagerDocument(
                email = email,
                otp = cls._generate()
            )
            obj.save()

        return otp

    @classmethod
    def check_otp(cls, otp, email):
        raise NotImplemented

    @classmethod
    def send_otp(cls, email, otp):
        user = UserDocument.objects.get(email=email)
        otp = cls.otp_generator(user.email)
        send_otp_via_email(otp, user.email)