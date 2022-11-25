import sys
import bcrypt

class PasswordManager:

    number_of_rounds = 16

    @classmethod
    def encode_password(cls, password):
        password = password.encode('utf-8')
        salt_object = bcrypt.gensalt(rounds=cls.number_of_rounds)
        resultant_hashed_str = bcrypt.hashpw(password, salt_object)
        return resultant_hashed_str

    @classmethod
    def compare_password(cls, password, encoded_password):
        password = password.encode('utf-8')
        encoded_password = encoded_password.encode('utf-8')
        if bcrypt.checkpw(password, encoded_password):
            return True
        return False