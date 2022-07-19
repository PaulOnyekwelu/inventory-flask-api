from werkzeug.security import safe_str_cmp
from .models.user import User

users = [User(1, "silanka", "asdf")]
username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}

print(username_mapping, userid_mapping)


def authenticate(username, password):
    print(username, password)
    user = username_mapping.get(username, None)
    if user and safe_str_cmp(password, user.password):
        print(user)
        return {"username": user.username, "id": user.id}


def identity(payload):
    userid = payload["identity"]
    return userid_mapping.get(user_id, None).id
