from urllib import request
from ..models import UserDocument

class AuthenticationService:

    def __init__(self, request):
        self.request = request

    def registerUser(self):

        try:
            if(email:=request.data.get("email")):
                UserDocument.objects.get(email=email)
            elif(phone:=request.data.get("phone")):
                UserDocument.objects.get(phone=phone)
        except UserDocument.DoesNotExist:
            UserDocument.objects.create(
                email=email if request.data.get("email") else None,
                phone=phone if request.data.get("phone") else None,
            )


    def loginUser(self):
        pass