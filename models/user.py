from mongoengine import Document, fields

class UserDocument(Document):
    email = fields.EmailField(unique=True)
    phone = fields.IntField(unique=True)
    password = fields.StringField(required=True)