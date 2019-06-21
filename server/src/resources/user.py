"""
Define the REST verbs relative to the users
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import UserRepository, UsersRepository
from util import parse_params


class UserResource(Resource):
    """ Verbs relative to the users """

    @staticmethod
    @swag_from("../swagger/user/GET.yml")
    def get(last_name, first_name):
        """ Return an user key information based on his name """
        user = UserRepository.get(last_name=last_name, first_name=first_name)
        return jsonify({"user": user.json})

    @staticmethod
    @parse_params(
        Argument("age", location="json", required=True, help="The age of the user.")
    )
    @swag_from("../swagger/user/POST.yml")
    def post(last_name, first_name, age):
        """ Create an user based on the sent information """
        user = UserRepository.create(
            last_name=last_name, first_name=first_name, age=age
        )
        return jsonify({"user": user.json})

    @staticmethod
    @parse_params(
        Argument("age", location="json", required=True, help="The age of the user.")
    )
    @swag_from("../swagger/user/PUT.yml")
    def put(last_name, first_name, age):
        """ Update an user based on the sent information """
        repository = UserRepository()
        user = repository.update(last_name=last_name, first_name=first_name, age=age)
        return jsonify({"user": user.json})

class UsersResource(Resource):
    @staticmethod
    @swag_from("../swagger/user/RECOMMEND.yml")
    def get(last_name, first_name):
        """ Return a recommendation for a user """
        list_of_marks = UsersRepository.recommend(last_name,first_name)
        l={}
        for i in list_of_marks:
            object = i.json
            l[object["movie"]]=object["value"]

        list_of_users = UsersRepository.get_all()
        users=[]
        for j in list_of_users :
            object2 = j.json
            users.append((object2["last_name"],object2["first_name"]))

        users_marks={}
        similarities=[]
        similarity_max=0
        for K in users :
            if K!=(last_name,first_name):
                list_of_marksK = UsersRepository.recommend(K[0],K[1])
                lK={}
                for iK in list_of_marksK:
                    objectK = iK.json
                    lK[objectK["movie"]]=objectK["value"]
                users_marks[K[0]]=lK
                s=UsersRepository.similarity(l,lK)
                similarities.append((K,s))
                if s>similarity_max:
                    similarity_max=s
                    similar_user=K

        list_of_marks_similar = users_marks[similar_user[0]]
        mark_max=0
        for movie in list_of_marks_similar.keys() :
            if movie not in l.keys():
                if list_of_marks_similar[movie]>mark_max:
                    mark_max=list_of_marks_similar[movie]
                    best_movie = movie

        return jsonify({"best_movie": best_movie})
