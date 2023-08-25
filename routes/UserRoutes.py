import json
from flask import Blueprint, request

from apiproject.service import UserService

user = Blueprint("user", __name__, template_folder='routes')

@user.route("/users", methods=["GET"])
def get_all_users():
    '''
    file: swagger/user/users.yml
    '''
    return UserService.get_all()

@user.route("/users", methods=["POST"])
def save_new_user():
    '''
    file: swagger/user/addUser.yml
    '''
    data = json.loads(request.get_data())
    return UserService.insert_one(data), 200

@user.route("/users", methods=["PATCH"])
def update_user():
    '''
    file: swagger/user/upUser.yml
    '''
    data = json.loads(request.get_data())
    return UserService.update_one(data), 200

@user.route('/users/<user_id>', methods=["DELETE"])
def deleteOne(user_id):
    '''
    file: swagger/user/delUser.yml
    '''
    return UserService.delete_one_by_id(user_id), 200

