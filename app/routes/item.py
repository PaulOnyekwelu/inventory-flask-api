from flask import request
from flask_restful import Resource

items = []


class Item(Resource):
    def get(self, name):
        item = next(filter(lambda x: x["name"] == name, items), None)
        return {"item": item}, 200 if item else 404

    def post(self, name):
        data = request.get_json(silent=True)
        if data is None:
            return {"msg": "required data not sent"}, 400
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item:
            return {"msg": "item already exist"}, 400
        if not data.get("price", None):
            return {"msg": "requires price field"}, 400
        item = {"name": name, "price": data["price"]}
        items.append(item)
        return {"item": item}, 201


class ItemList(Resource):
    def get(self):
        return {"items": items}
