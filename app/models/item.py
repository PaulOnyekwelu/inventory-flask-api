import sqlite3
from app.utils.constants import DB_URI


class ItemModel():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def find_item_by_name(cls, name):
        connection = sqlite3.connect(DB_URI)
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        item = result.fetchone()
        connection.close()

        item = cls(*item) if item else None
        return item.__dict__ if item else None

    @classmethod
    def insert(cls, item):
        connection = sqlite3.connect(DB_URI)
        cursor = connection.cursor()

        query = "INSERT INTO items VALUES (?, ?)"
        result = cursor.execute(query, (item["name"], item["price"]))
        connection.commit()
        connection.close()

        return True

    @classmethod
    def update(cls, item):
        connection = sqlite3.connect(DB_URI)
        cursor = connection.cursor()

        query = "UPDATE items SET price=?  WHERE name=?"
        result = cursor.execute(query, (item["price"], item["name"]))
        connection.commit()
        connection.close()

        return True

    @classmethod
    def delete(cls, name):
        connection = sqlite3.connect(DB_URI)
        cursor = connection.cursor()

        query = "DELETE FROM items WHERE name=?"
        cursor.execute(query, (name,))
        connection.commit()
        connection.close()
        return True

    @classmethod
    def get_all_items(cls):
        connection = sqlite3.connect(DB_URI)
        cursor = connection.cursor()

        query = "SELECT * FROM items"
        result = cursor.execute(query)
        items = result.fetchall()
        connection.commit()
        connection.close()
        items = [{"name": x[0], "price": x[1]} for x in items]

        return items
