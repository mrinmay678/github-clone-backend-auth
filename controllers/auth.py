from flask import request
from flask_restful import Resource

class Authentication(Resource):

    def register(self):
        data = request.json
        return data

    def login(self):
        pass

    def post(self, service: str):
        if service == "register":
            return self.register(), 201
        elif service == "login":
            return self.login(), 200
        else:
            raise Exception("Service Not Found", 404)