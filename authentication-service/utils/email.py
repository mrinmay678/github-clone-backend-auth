from main import mail
from flask_mail import Message

def send_email(subject: str, recipents: list, body: str):
    msg = Message(
        subject=subject,
        sender="mrinmay.works@gmail.com",
        recipients=recipents
    )
    msg.body = body
    mail.send(msg)