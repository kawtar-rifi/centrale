"""
Define the REST verbs relative to the movies
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import MarkRepository
from util import parse_params


class MarkResource(Resource):
    """ Verbs relative to the marks """

    @staticmethod
    @swag_from("../swagger/mark/GET.yml")
    def get(movie, user_first_name, user_last_name):
        """ Return an mark key information based on its movie and its user """
        mark = MarkRepository.get(movie=movie, user_first_name=user_first_name, user_last_name=user_last_name)
        return jsonify({"mark": mark.json})

    @staticmethod
    @parse_params(
        Argument("value", location="json", required=True, help="The value of the mark.")
    )
    @swag_from("../swagger/mark/POST.yml")
    def post(movie, user_first_name, user_last_name, value):
        """ Create a mark based on the sent information """
        mark = MarkRepository.create(movie=movie, user_first_name=user_first_name, user_last_name=user_last_name, value=value)
        return jsonify({"mark": mark.json})

    @staticmethod
    @parse_params(
        Argument("value", location="json", required=True, help="The value of the mark.")
    )
    @swag_from("../swagger/mark/PUT.yml")
    def put(movie, user_first_name, user_last_name, value):
        """ Update a mark based on the sent information """
        repository = MarkRepository()
        mark = repository.update(movie=movie, user_first_name=user_first_name, user_last_name=user_last_name, value=value)
        return jsonify({"mark": mark.json})
