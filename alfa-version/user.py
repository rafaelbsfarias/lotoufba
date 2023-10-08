class User:
    def __init__(self, username, is_admin=False):
        self.username = username
        self.is_admin = is_admin

    def __str__(self):
        return f"Username: {self.username}, Admin: {self.is_admin}"
