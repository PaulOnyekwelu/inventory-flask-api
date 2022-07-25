import sqlite3
import os
from flask_sqlalchemy import SQLAlchemy, inspect

from utils.constants import DB_NAME


class DBModel:
    db = SQLAlchemy()

    @classmethod
    def initialize(cls, app):
        cls.db.init_app(app)
        cls.create_tables()
        # print("logging app =>", app.app_context)
        # inspector = inspect(cls.db.engine)
        # with app.app_context():
        #     if (inspector.has_table("users")):
        #         cls.db.create_all()

    @classmethod
    def create_tables(cls):
        print("uri ====> ", DB_NAME)
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()

        users_query = """CREATE TABLE IF NOT EXISTS users (
              id INTEGER PRIMARY KEY,
              username VARCHAR(50),
              password TEXT
          )
          """
        items_query = """CREATE TABLE IF NOT EXISTS items (
              id INTEGER PRIMARY KEY,
              name VARCHAR(50),
              price real
          )
          """

        cursor.execute(users_query)
        cursor.execute(items_query)
        connection.commit()
        connection.close()
