from passlib.hash import pbkdf2_sha512
import re

class Utils(object):

    @staticmethod
    def hash_password(password):
        hash1 = pbkdf2_sha512.encrypt(password)
        return hash1

    @staticmethod
    def check_hashed_password(password, hashed_password):
        check_password = pbkdf2_sha512.verify(password, hashed_password)
        return check_password

    @staticmethod
    def check_password(password, hashed_password):
         if password == hashed_password:
             return True
         else:
             return False

    @staticmethod
    def email_is_valid(email):
        email_address_matcher = re.compile('^[\w-]+@([\w-]+\.)+[\w]+$')
        return True if email_address_matcher.match(email) else False
