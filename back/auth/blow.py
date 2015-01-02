__author__ = 'Steven'

from django.conf import settings
from django.contrib.auth.models import Permission, User
import csv, bcrypt

class Auth(object):
    def authenticate(self, username=None, password=None):
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return user
            if self.checkInPasswd(username, password):
                user.set_password(password)
                user.save()
                return user
        except User.DoesNotExist:
            if self.checkInPasswd(username, password):
                user = User(username=username)
                user.set_password(password)
                #user.is_staff = True
                #user.is_superuser = True
                user.save()
                return user
        return None

    def checkHash(self, encrypted, plain):
        #try:
        if bcrypt.hashpw(plain, encrypted) == encrypted:
            return True
        #except Exception:
        #    return False
        return False

    def checkInPasswd(self, login, password):
        with open(getattr(settings, 'PASSWORD_FILE', 'password.blowfish'), 'r') as f:
            reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
            for row in reader:
                if row[0] == login:
                    return self.checkHash(row[1].encode('utf-8'), password.encode('utf-8'))
        return False

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None