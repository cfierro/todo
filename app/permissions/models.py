from app import db, Base

from app.lib.models import TableMixin


class TodoListPermission(TableMixin, Base):
    __tablename__ = 'todo_list_permission'

    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    todoListId = db.Column(db.Integer, db.ForeignKey('todo_list.id'))

    user = db.relationship('User')
    todoList = db.relationship('TodoList')

    def __init__(self, userId, todoListId):
        """Constructor.

        Args:
            userId - ID of user allowed to view the given todo list.
            todoListId - ID of todo list being granted access to.
        """
        self.userId = userId
        self.todoListId = todoListId
