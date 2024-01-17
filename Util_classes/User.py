
from Util_classes.Server_handler.user_Authentication import check_token, gen_token
import random


class User:

    def __init__(self):
        self.is_authenticated: bool = False
        self.is_guest: bool = False
        self._Username: str = ""
        self._ID: int = -1
        self._token: str = ""

        with open("userconfig.txt", mode="r") as config:
            username = config.readline().rstrip()
            ID = config.readline().rstrip()
            token = config.readline().rstrip()

            if username:
                self._Username = username
            if ID:
                self._ID = int(ID)
            if token:
                self._token = token

    def register_guest(self):
        self._Username = "Guest#" + str(random.randint(10000000, 99999999))
        self._token = gen_token()
        self._ID = random.randint(10000, 99999)
        self.is_guest = True
        print(self._token)

    def is_user_authenticated(self):
        if self.is_guest:
            self.is_authenticated = True
            return True
        else:
            self.is_authenticated = check_token(self._Username, self._ID, self._token)
            return self.is_authenticated

    def get_username(self):
        return self._Username


