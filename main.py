from settings import ExtendedAPI
from flask import Flask, make_response
from urls import urlpatterns
from utils.response import Response

app = Flask(__name__)
api = ExtendedAPI(app)

@api.representation('application/json')
def custom_response(data, code=200, headers={}):
    res = Response.success(data)
    resp = make_response(res, code)
    resp.headers.extend(headers)
    return resp

for pattern in urlpatterns:
    api.add_resource(
        pattern.resource,
        pattern.route,
        endpoint=pattern.name
    )
