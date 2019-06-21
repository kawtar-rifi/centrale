""" Defines the User repository """

from models import User, Mark
from math import sqrt


class UserRepository:
    """ The repository for the user model """

    @staticmethod
    def get(last_name, first_name):
        """ Query a user by last and first name """
        return User.query.filter_by(last_name=last_name, first_name=first_name).one()

    def update(self, last_name, first_name, age):
        """ Update a user's age """
        user = self.get(last_name, first_name)
        user.age = age

        return user.save()

    @staticmethod
    def create(last_name, first_name, age):
        """ Create a new user """
        user = User(last_name=last_name, first_name=first_name, age=age)

        return user.save()


class UsersRepository:
    """The repository for the recommendation"""
    @staticmethod
    def recommend(last_name, first_name):
        """Give a recommendation to a user"""
        d= Mark.query.filter_by(user_last_name=last_name, user_first_name=first_name)
        return d

    @staticmethod
    def get_all():
        """Query all the movies"""
        return User.query.all()

    @staticmethod
    def similarity(l1,l2):
        S=0
        N1=0
        N2=0
        for i in l1.keys():
            N1+= l1[i]*l1[i]
            for j in l2.keys():
                if j==i:
                    S+= l2[j]*l1[i]
        for k in l2.keys():
            N2+= l2[k]*l2[k]

        if l1!={} and l2!={}:
            similarity = S/(sqrt(N1)*sqrt(N2))
        else :
            similarity = 0
        return similarity

