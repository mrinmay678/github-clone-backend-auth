from mongoengine import Document, fields, EmbeddedDocument

class CompanyDetail(EmbeddedDocument):
    name = fields.StringField()
    website = fields.StringField()
    email = fields.EmailField()

class ProfileDocument(Document):
    user_id = fields.StringField(unique=True, required=True)
    first_name = fields.StringField(required=True)
    last_name = fields.StringField()
    company = fields.EmbeddedDocumentField(CompanyDetail)
    bio = fields.StringField()