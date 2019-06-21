"""
Define the REST verbs relative to the users
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import MovieRepository
from repositories import MoviesRepository
from util import parse_params


class MovieResource(Resource):
    """ Verbs relative to the movies """

    @staticmethod
    @swag_from("../swagger/movie/GET.yml")
    def get(title):
        """ Return a movie key information based on the title """
        movie = MovieRepository.get(title=title)
        return jsonify({"movie": movie.json})

    @staticmethod
    @parse_params(
        Argument("producer", location="json", required=True, help="The producer of the movie."),
        Argument("date", location="json", required=True, help="The date of the movie."),
        Argument("actor", location="json", required=True, help="The main actor in the movie.")
    )
    @swag_from("../swagger/movie/POST.yml")
    def post(title, producer, date, actor):
        """ Create a movie based on the sent information """
        movie = MovieRepository.create(
            title=title, producer=producer, date=date, actor=actor
        )
        return jsonify({"movie": movie.json})

    @staticmethod
    @parse_params(
        Argument("producer", location="json", required=True, help="The producer of the movie."),
        Argument("date", location="json", required=True, help="The date of the movie."),
        Argument("actor", location="json", required=True, help="The main actor in the movie.")
    )
    @swag_from("../swagger/movie/PUT.yml")
    def put(title, producer, date, actor):
        """ Update a movie based on the sent information """
        repository = MovieRepository()
        movie = repository.update(title=title, producer=producer, date=date, actor=actor)
        return jsonify({"movie": movie.json})

class MoviesResource(Resource):

    @staticmethod
    @swag_from("../swagger/movie/GET_ALL.yml")
    def get():
        """Return all the movies"""
        list_of_movies = MoviesRepository.get_all()
        l=[]
        for j in list_of_movies :
            object = j.json
            l.append(object)
        return jsonify({"list_of_movies":l})
