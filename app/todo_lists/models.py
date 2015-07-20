from app import db


class TodoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    user = db.relationship('User',
        backref=db.backref('lists', lazy='dynamic'))

    def __init__(self, name, userId, id=None):
        self.id = id
        self.name = name
        self.userId = userId
