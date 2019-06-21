"""
Defines the blueprint for the movies
"""
from flask import Blueprint
from flask_restful import Api

from resources import MovieResource
from resources import MoviesResource

MOVIE_BLUEPRINT = Blueprint("movie", __name__)
Api(MOVIE_BLUEPRINT).add_resource(
    MovieResource, "/movie/<string:title>"
)

MOVIES_BLUEPRINT = Blueprint("list_of_movies",__name__)
Api(MOVIES_BLUEPRINT).add_resource(
    MoviesResource, "/movies/"
)
