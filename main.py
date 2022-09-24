from settings import ExtendedAPI, CustomResponse
from flask import Flask
from urls import urlpatterns

app = Flask(__name__)

app.response_class = CustomResponse

api = ExtendedAPI(app)

for pattern in urlpatterns:
    api.add_resource(
        pattern.resource,
        pattern.route,
        endpoint=pattern.name
    )
