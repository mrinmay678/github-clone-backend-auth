from mongoengine import Document, fields
from datetime import datetime

class UserDocument(Document):
    username = fields.StringField(unique=True)
    email = fields.EmailField(unique=True)
    password = fields.StringField(required=True)

    def save(self, *args, **kwargs):
        timestamp = datetime.timestamp()
        email = self.email.split("@")[0]
        self.username = email + str(timestamp)
        return super().save(*args, **kwargs)