from datetime import datetime

from db import DBModel

db = DBModel.db


class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    items = db.relationship("ItemModel", backref="store", lazy="dynamic")
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, name):
        self.name = name

    def save_store(self):
        db.session.add(self)
        db.session.commit()

    def json(self):
        return {
            "name": self.name,
            "items": [item.json() for item in self.items.all()],
            "create_at": str(self.created_at),
            "updated_at": str(self.updated_at)
        }

    def delete_store(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_store_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def get_all_stores(cls):
        return cls.query.all()
