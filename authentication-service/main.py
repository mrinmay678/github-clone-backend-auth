from settings import ExtendedAPI, MailConfig
from flask import Flask, make_response
from urls import urlpatterns
from utils.response import Response
from flask_mail import Mail

app = Flask(__name__)
api = ExtendedAPI(app)

app.config['MAIL_SERVER'] = MailConfig.SERVER
app.config['MAIL_PORT'] = MailConfig.PORT
app.config['MAIL_USERNAME'] = MailConfig.USERNAME
app.config['MAIL_PASSWORD'] = MailConfig.PASSWORD
app.config['MAIL_USE_TLS'] = MailConfig.USE_TLS
app.config['MAIL_USE_SSL'] = MailConfig.USE_SSL

mail = Mail(app)

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
