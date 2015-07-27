from app import db

from app.lib.models import Base


class TodoList(Base):
    name = db.Column(db.String)
    creatorId = db.Column(db.Integer, db.ForeignKey('user.id'))
    creator = db.relationship(
        'User', backref=db.backref('lists', lazy='dynamic'))

    def __init__(self, name, creatorId):
        self.name = name
        self.creatorId = creatorId
