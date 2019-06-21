""" Defines the Movie repository """

from models import Movie


class MovieRepository:
    """ The repository for the movie model """

    @staticmethod
    def get(title):
        """ Query a movie by title """
        return Movie.query.filter_by(title=title).one()


    def update(self, title, producer, date, actor):
        """ Update a movie's information """
        movie = self.get(title)
        movie.producer = producer
        movie.date = date
        movie.actor = actor

        return movie.save()

    @staticmethod
    def create(title, producer, date, actor):
        """ Create a new movie """
        movie = Movie(title=title, producer=producer, date=date, actor=actor)

        return movie.save()


class MoviesRepository:
    """The repository for the list of movies"""
    @staticmethod
    def get_all():
        """Query all the movies"""
        return Movie.query.all()
