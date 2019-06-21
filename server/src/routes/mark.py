"""
Defines the blueprint for the movies
"""
from flask import Blueprint
from flask_restful import Api

from resources import MarkResource

MARK_BLUEPRINT = Blueprint("mark", __name__)
Api(MARK_BLUEPRINT).add_resource(
    MarkResource, "/mark/<string:movie>/<string:user_first_name>/<string:user_last_name>"
)
