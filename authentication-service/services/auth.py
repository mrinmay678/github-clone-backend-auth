from utils.password_manager import PasswordManager
from models import UserDocument
from mongoengine.errors import DoesNotExist

class AuthenticationService:

    @classmethod
    def register_user(cls, email: str, password: str):
        try:
            UserDocument.objects.get(email=email)
            raise Exception("User Already Exist")
        except UserDocument.DoesNotExist:
            obj = UserDocument.objects.create(
                email=email,
                password=PasswordManager.encode_password(password)
            )
            obj.save()
        return {
            "email": obj.email,
        }

    @classmethod
    def login_user(cls, email: str, password: str):
        user = UserDocument.objects.get(email=email)
        if not PasswordManager.compare_password(password, user.password):
            raise Exception("Incorrect Password", 401)
        return {
            "email": user.email,
        }
