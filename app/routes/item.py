from flask import request
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

items = []


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("price", required=True, type=float,
                        help="Field is required")

    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x["name"] == name, items), None)
        return {"item": item}, 200 if item else 404

    @jwt_required()
    def post(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item:
            return {"msg": "item already exist"}, 400
        data = Item.parser.parse_args()
        data = request.get_json(silent=True)
        if data is None:
            return {"msg": "required data not sent"}, 400
        if not data.get("price", None):
            return {"msg": "requires price field"}, 400
        item = {"name": name, "price": data["price"]}
        items.append(item)
        return {"item": item}, 201

    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        item = next(filter(lambda x: x["name"] == name, items), None)
        if item:
            item.update(data)
        else:
            item = {"name": name, "price": data["price"]}
            items.append(item)
        return item

    @jwt_required()
    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {"msg": "item deleted"}, 200


class ItemList(Resource):
    @jwt_required()
    def get(self):
        return {"items": items}
