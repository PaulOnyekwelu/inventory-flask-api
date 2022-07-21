from flask import request
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from app.models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("price", required=True, type=float,
                        help="Field is required")

    @jwt_required()
    def get(self, name):
        try:
            item = ItemModel.find_item_by_name(name)
        except Exception:
            return {"message": "There was an error"}, 500
        return {"item": item}, 200 if item else 404

    @jwt_required()
    def post(self, name):
        try:
            if ItemModel.find_item_by_name(name):
                return {"msg": "item already exist"}, 400

            data = Item.parser.parse_args()
            item = {"name": name, "price": data["price"]}
            ItemModel.insert(item)
            return {"item": item}, 201

        except Exception:
            return {"message": "There was an error"}, 500

    @jwt_required()
    def put(self, name):

        data = Item.parser.parse_args()
        item = ItemModel.find_item_by_name(name)
        update_item = {"name": name, "price": data["price"]}
        if item:
            ItemModel.update(update_item)
        else:
            ItemModel.insert(update_item)
        return update_item, 200

    @jwt_required()
    def delete(self, name):
        try:
            ItemModel.delete(name)
        except Exception:
            return {"message": "There was an error"}, 500
        return {"msg": "item deleted"}, 200


class ItemList(Resource):
    @jwt_required()
    def get(self):
        items = ItemModel.get_all_items()
        return {"items": items}
