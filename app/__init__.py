import os
from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from .routes.item import Item, ItemList
from .auth_func import authenticate, identity

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")

if __name__ == "__main__":
    app.run()