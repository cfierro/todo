from app import db, Base

from app.lib.models import TableMixin


class Todo(TableMixin, Base):

    __tablename__ = 'todo'

    subject = db.Column(db.String)
    todoListId = db.Column(db.Integer, db.ForeignKey('todo_list.id'))
    dueDate = db.Column(db.DateTime)
    description = db.Column(db.Text)
    priority = db.Column(db.Integer)
    completed = db.Column(db.Boolean)
    assigneeId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

    assignee = db.relationship('User', backref=db.backref('assignedTodos'))
    todoList = db.relationship('TodoList', backref=db.backref('todos'))

    def __init__(self, subject, todoListId, dueDate=None, description="",
                 priority=3, completed=False, assigneeId=None):
        self.subject = subject
        self.todoListId = todoListId
        self.dueDate = dueDate
        self.description = description
        self.priority = priority
        self.completed = completed
        self.assigneeId = assigneeId

    def toDict(self):
        """Method to convert a todo object into a dictionary.
        """
        return {
                'id': self.id,
                'subject': self.subject,
                'dueDate': self.dueDate,
                'description': self.description,
                'priority': self.priority,
                'completed': self.completed,
                'assignee': self.assignee.name,
                'list': self.todoList.name
            }
