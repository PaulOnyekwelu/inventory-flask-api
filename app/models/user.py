import sqlite3
from app.utils.constants import DB_URI


class UserModel():
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect(DB_URI)
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username, ))
        user = result.fetchone()
        connection.close()

        user = cls(*user) if user else None
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect(DB_URI)
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,))
        user = result.fetchone()
        connection.close()

        user = cls(*user) if user else None
        return user
