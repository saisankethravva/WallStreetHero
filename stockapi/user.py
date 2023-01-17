from flask_login import (
    UserMixin)


class User(UserMixin):
    def __init__(self, email: str, fn: str, ln: str, user_id, role_id=1):
        self.email = email
        self.fn = fn
        self.ln = ln
        self.role_id = role_id
        self.id = 2
        self.user_id = user_id

    def get_id(self):
        ## get id from db
        return self.email
