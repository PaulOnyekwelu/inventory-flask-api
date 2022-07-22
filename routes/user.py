import sqlite3
from flask_restful import Resource, reqparse

from models.user import UserModel
from utils.constants import DB_URI


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", required=True,
                        type=str, help="field is required!")
    parser.add_argument("password", required=True,
                        type=str, help="field is required!")

    @classmethod
    def post(cls):
        data = cls.parser.parse_args()

        user = UserModel.find_by_username(data["username"])
        if user:
            return {"message": "User already exist"}, 400

        connection = sqlite3.connect(DB_URI)
        cursor = connection.cursor()

        query = "INSERT INTO users VALUES (NULL, ?, ?)"
        cursor.execute(query, (data["username"], data["password"]))
        connection.commit()
        connection.close()

        return {"message": "user created successfully..."}, 201
