
from . import db
from .abc import BaseModel, MetaBaseModel

class Movie(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The Movie model """

    __tablename__ = "movie"

    title = db.Column(db.String(300), primary_key=True)
    producer = db.Column(db.String(300))
    date = db.Column(db.Integer, nullable=True)
    actor = db.Column(db.String(300))

    def __init__(self, title, producer=None, date=None, actor=None):
        """ Create a new Movie """
        self.title = title
        self.producer = producer
        self.date = date
        self.actor = actor
