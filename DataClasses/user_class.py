"""This is to set up a user access to the site"""
class User:
    """User Class"""
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_password(self):
        return self._password

    def hide_password(self):
        """Encrypt the password"""
        pass

    def check_password(self, password):
        """Checks password for requirements"""
        if len(password) > 7:
            self._password = password
        else:
            return "Password was rejected"
