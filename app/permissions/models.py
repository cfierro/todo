from app import db

from app.lib.models import Base


class TodoListPermission(Base):
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    todoListId = db.Column(db.Integer, db.ForeignKey('todoList.id'))

    def __init__(self, userId, todoListId):
        self.userId = userId
        self.todoListId = todoListId
