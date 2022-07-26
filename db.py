import sqlite3
import os
from flask_sqlalchemy import SQLAlchemy, inspect

from utils.constants import DB_NAME


class DBModel:
    db = SQLAlchemy()

    def __init__(self, app):
        DBModel.db.init_app(app)
        self.app = app

    def create_tables(self):
        DBModel.db.create_all()
