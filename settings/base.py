from .error_handling import get_exc
from .config import MONGO_USERNAME, MONGO_PASSWORD, MONGO_HOST, MONGO_PORT, MONGO_DB
from flask_restful import Api
from utils.response import Response


class ExtendedAPI(Api):
    """This class overrides 'handle_error' method of 'Api' class ,
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
    MONGO: Mongo = Mongo()
