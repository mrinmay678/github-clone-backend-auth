from datetime import datetime, timedelta
from mongoengine import Document, fields, EmbeddedDocument

class OtpManagerDocument(Document):

    def _get_default_expiry(self):
        return datetime.now() + timedelta(minutes=5)

    email = fields.StringField(required=True, unique=True)
    otp = fields.IntField(required=True)
    expiry = fields.DateTimeField(default=_get_default_expiry) # 5 mins Expiry
