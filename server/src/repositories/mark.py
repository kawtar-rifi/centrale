""" Defines the Mark repository """

from models import Mark


class MarkRepository:
    """ The repository for the mark model """

    @staticmethod
    def get(movie, user_first_name, user_last_name):
        """ Query a mark by its movie and its user """
        return Mark.query.filter_by(movie=movie, user_first_name=user_first_name, user_last_name=user_last_name).one()

    def update(self, movie, user_first_name, user_last_name, value):
        """ Update mark's information """
        mark = self.get(movie, user_first_name, user_last_name)
        mark.value = value
        return mark.save()

    @staticmethod
    def create(movie, user_first_name, user_last_name, value):
        """ Create a new mark """
        mark = Mark(movie=movie, user_first_name=user_first_name, user_last_name=user_last_name, value=value)

        return mark.save()

