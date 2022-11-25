from .error_handling import get_exc
from .config import *
from flask_restful import Api
from utils.response import Response

class Jwt:
    """
    This class maintains headers and signature for JWT Authentication
    """

    secret = "it_is_a_secret"
    algorithm = "HS256"

class ExtendedAPI(Api):
    """
    This class overrides 'handle_error' method of 'Api' class ,
    to extend global exception handing functionality of 'flask-restful'.
    """

    def handle_error(self, error: Exception):
        """It helps preventing writing unnecessary
        try/except block though out the application
        """
        message, code = get_exc(error)
        return Response.error(message, code)


class Mongo:
    """
    This Class is Used to manage Mongo Credentials for Connection
    """

    HOST: str = MONGO_HOST
    USERNAME: str = MONGO_USERNAME
    PASSWORD: str = MONGO_PASSWORD
    PORT: str = MONGO_PORT
    DB: str = MONGO_DB


class DATABASE:
    """
    This Class is Used to manage Database Connections
    """
    MONGO: Mongo = Mongo()

class MailConfig:
    """
    This Class is Used to manage SMTP Server Configuration
    """
    SERVER: str = MAIL_SERVER
    PORT: int = MAIL_PORT
    USERNAME: str = MAIL_USERNAME
    PASSWORD: str = MAIL_PASSWORD
    USE_TLS: bool = MAIL_USE_TLS
    USE_SSL: bool = MAIL_USE_SSL