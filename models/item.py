import sqlite3
from utils.constants import DB_URI
from db import db


class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save_item(self):
        db.session.add(self)
        db.session.commit()

    def delete_item(self):
        db.session.delete(self)
        db.session.commit()

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
        }

    @classmethod
    def find_item_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def get_all_items(cls):
        return cls.query.all()
