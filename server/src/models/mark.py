"""
Define the Mark model
"""
from . import db
from .abc import BaseModel, MetaBaseModel
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class Mark(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The Mark model """

    __tablename__ = "mark"

    movie = db.Column(db.String(300), primary_key=True)
    user_first_name = db.Column(db.String(300), primary_key=True)
    user_last_name = db.Column(db.String(300), primary_key=True)
    value = db.Column(db.Integer, nullable=True)
    #movie_title = Column(Integer, ForeignKey("movie.title"))
    #user_first_name = Column(Integer, ForeignKey("user.first_name"))
    #user_last_name = Column(Integer, ForeignKey("user.last_name"))


    def __init__(self, movie, user_first_name, user_last_name, value=None):
        """ Create a new mark of a movie from a user """
        self.movie = movie
        self.user_first_name = user_first_name
        self.user_last_name = user_last_name
        self.value = value

