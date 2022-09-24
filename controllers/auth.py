from flask import request
from flask_restful import Resource
from utils.response import Response

class Authentication(Resource):

    def register(self):
        data = request.json
        return data

    def login(self):
        pass

    def post(self, service: str):
        if service == "register":
            return Response.success(self.register(), 201)
        elif service == "login":
            return Response.success(self.login(), 200)
        else:
            raise Exception("Service Not Found", 404)