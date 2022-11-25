from utils.email import send_email

def send_otp_via_phone(otp, phone):
    raise NotImplemented

def send_otp_via_email(otp, email):
    recipent: list = [email]
    body: str = f"""
    OTP - {otp}
    """
    send_email("OTP for Verification", recipents=recipent, body=body)