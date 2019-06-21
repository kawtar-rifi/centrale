"""
Defines the blueprint for the users
"""
from flask import Blueprint
from flask_restful import Api

from resources import UserResource, UsersResource

USER_BLUEPRINT = Blueprint("user", __name__)
Api(USER_BLUEPRINT).add_resource(
    UserResource, "/user/<string:last_name>/<string:first_name>"
)

USERS_BLUEPRINT = Blueprint("best_movie", __name__)
Api(USERS_BLUEPRINT).add_resource(
    UsersResource, "/users/<string:last_name>/<string:first_name>"
)
