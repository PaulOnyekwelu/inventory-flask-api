from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.store import StoreModel


class Store(Resource):
    @jwt_required()
    def get(self, name):
        store = StoreModel.find_store_by_name(name)
        if store:
            return store.json()
        return {"msg": "store not found"}, 400

    @jwt_required()
    def post(self, name):
        store = StoreModel.find_store_by_name(name)
        if store:
            return {"msg": "store already exist"}, 400
        store = StoreModel(name)
        try:
            store.save_store()
        except Exception:
            return {"msg": "unable to add store"}, 500
        return {"msg": "store successfully created..."}

    @jwt_required()
    def delete(self, name):
        store = StoreModel.find_store_by_name(name)
        if store is None:
            return {"msg": "store not found"}, 400
        try:
            store.delete_store()
        except Exception as err:
            print(err)
            return {"msg": "unable to delete"}, 500
        return {"msg": "store deleted successfully"}


class StoreList(Resource):
    @jwt_required()
    def get(self):
        stores = StoreModel.get_all_stores()
        return {"stores": [store.json() for store in stores]}
