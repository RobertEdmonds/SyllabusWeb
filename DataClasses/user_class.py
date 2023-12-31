"""This is to set up a user access to the site"""
import re
import sqlite3

connection = sqlite3.connect(":memory:")

cursor = connection.cursor()

sql_file = open("lib/create.sql")

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
        password_regex = re.compile(r"^(([A-Z]){1,}|([a-z]){1,}|([0-9]){1,}|(\W){1,}){8,}$")
        if len(password) > 7:
            self._password = password
        else:
            return "Password was rejected"
