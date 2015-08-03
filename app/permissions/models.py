from app import db, Base

from app.lib.models import TableMixin


class TodoListPermission(TableMixin, Base):

    __tablename__ = 'todo_list_permission'

    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    todoListId = db.Column(db.Integer, db.ForeignKey('todo_list.id'))

    def __init__(self, userId, todoListId):
        self.userId = userId
        self.todoListId = todoListId
