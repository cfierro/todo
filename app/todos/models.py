from app import db, Base

from app.lib.models import TableMixin


class Todo(TableMixin, Base):

    __tablename__ = 'todo'

    subject = db.Column(db.String)
    todoListId = db.Column(db.Integer, db.ForeignKey('todo_list.id'))
    creatorId = db.Column(db.Integer)
    dueDate = db.Column(db.DateTime)
    description = db.Column(db.Text)
    priority = db.Column(db.Integer)
    completed = db.Column(db.Boolean)
    assigneeId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

    assignee = db.relationship('User', backref=db.backref('assignedTodos'))
    todoList = db.relationship('TodoList', backref=db.backref('todos'))

    def __init__(self, subject, todoListId, creatorId, dueDate=None, description="",
                 priority=3, completed=False, assigneeId=None):
        self.subject = subject
        self.todoListId = todoListId
        self.creatorId = creatorId
        self.dueDate = dueDate
        self.description = description
        self.priority = priority
        self.completed = completed
        self.assigneeId = assigneeId

    def toDict(self):
        """Method to convert a todo object into a dictionary.
        """
        assigneeName = self.assignee.name if self.assigneeId else None

        return {
            'id': self.id,
            'subject': self.subject,
            'todoListId': self.todoListId,
            'creatorId': self.creatorId,
            'dueDate': self.dueDate,
            'description': self.description,
            'priority': self.priority,
            'completed': self.completed,
            'assignee': assigneeName,
            'list': self.todoList.name
        }
