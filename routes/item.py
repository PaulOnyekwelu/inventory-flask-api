from flask import request
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import json

from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("price", required=True, type=float,
                        help="Field is required")

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_item_by_name(name)
        print(dir(item))
        if item:
            return item.json()
        return {"msg": "item not found"}, 404

    @jwt_required()
    def post(self, name):
        data = Item.parser.parse_args()
        if ItemModel.find_item_by_name(name):
            return {"msg": "item already exist"}, 400

        item = ItemModel(name, data['price'])
        try:
            item.save_item()
        except Exception:
            return {"message": "There was an error"}, 500

        return item.json(), 201

    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_item_by_name(name)
        if item is None:
            item = ItemModel(name, data["price"])
        item.price = data["price"]
        try:
            item.save_item()
        except Exception:
            return {"message": "There was an error"}, 500

        return item.json(), 200

    @jwt_required()
    def delete(self, name):
        item = ItemModel.find_item_by_name(name)

        if item is None:
            return {"msg": "item does not exist"}, 400
        try:
            item.delete_item()
        except Exception:
            return {"message": "Unable to delete item"}, 500
        return {"msg": "item deleted"}, 200


class ItemList(Resource):
    @jwt_required()
    def get(self):
        result = []
        items = ItemModel.get_all_items()
        return {"items": [item.json() for item in items]}
