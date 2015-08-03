from app import db, Base

from app.lib.models import TableMixin


class TodoList(TableMixin, Base):

    __tablename__ = 'todo_list'

    name = db.Column(db.String)
    creatorId = db.Column(db.Integer, db.ForeignKey('user.id'))
    creator = db.relationship(
        'User', backref=db.backref('lists', lazy='dynamic'))

    def __init__(self, name, creatorId):
        self.name = name
        self.creatorId = creatorId
