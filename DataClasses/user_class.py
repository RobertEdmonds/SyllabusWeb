"""This is to set up a user access to the site"""
class User:
    """User Class"""
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def hide_password(self):
        """Encrypt the password"""
        pass
