import json
from flask import Blueprint, request

from api.helper.user_crud import (get_all_users, add_a_users, get_single_user,
                                  update_single_user)

USER_BLUEPRINT = Blueprint('user', __name__, url_prefix='/api/')


@USER_BLUEPRINT.route("/user", methods=["GET", "POST"])
def get_users():
    if request.method == "POST":
        data = json.loads(request.data)
        return add_a_users(data)
    return get_all_users()


@USER_BLUEPRINT.route("/user/<int:id>", methods=["GET", "PUT", "PATCH"])
def update_user(id):
    if request.method == "PUT" or request.method == "PATCH":
        data = json.loads(request.data)
        return update_single_user(id, data)
    if request.method == "DELETE":
        pass
    return get_single_user(id)
