# Ask about getting branches up to date once committed

import json

from flask import request
from flask_restful import Resource

from app import db, Todo
from app.lib.response_util import buildOkResponse


def _returnTodo(todo):
    """Private method to convert a todo object into a dictionary.

    Args:
        todo - A todo model.
    """
    return {
            "id": todo.id,
            "subject": todo.subject
        }


class todoMultiResource(Resource):
    """Class for creating and accessing todos.
    """
    def get(self):  # Should this take a user and return their todos?
        """Method gets a list of all the todos and returns them in an OK
        response.
        """
        todos = Todo.query.all()

        return buildOkResponse([_returnTodo(todo) for todo in todos])

    def post(self):
        """Method adds a new todo.
        """
        newTodoData = json.loads(request.form['data'])  # this is a dictionary
        newTodo = Todo(newTodoData['subject'], newTodoData['todoListId'],
                       newTodoData['dueDate'], newTodoData['description'],
                       newTodoData['creatorId'], newTodoData['priority'],
                       newTodoData['completed'], newTodoData['assigneeId'])
        db.session.add(newTodo)
        db.session.commit()

        return buildOkResponse(_returnTodo(newTodo))


class todoResource(Resource):
    """Class for updating, delelting, getting single todo.
    """
    def put(self, todoId):
        """Method updates a todo information and returns todo in an OK response.

        Args:
            todoId - Interger, primary key identifying the todo.
        """
        todo = Todo.query.get(todoId)
        todoData = json.loads(request.form['data'])

        todo.subject = todoData.get('subject') or todo.subject
        todo.dueDate = todoData.get('dueDate') or todo.dueDate
        todo.description = todoData.get('description') or todo.description
        todo.priority = todoData.get('priority') or todo.priority
        todo.completed = todoData.get('completed') or todo.completed
        todo.assigneeId = todoData.get('assigneeId') or todo.assigneeId

        db.session.commit()

        return buildOkResponse(_returnTodo(todo))

    def get(self, todoId):
        """Method gets and returns a single todo in an OK response.
        """
        todo = Todo.query.get(todoId)
        return buildOkResponse(_returnTodo(todo))

    def delete(self, todoId):
        """Method deletes a todo and returns result none.
        """
        todo = Todo.query.get(todoId)
        db.session.delete(todo)
        db.session.commit()

        return buildOkResponse(None)
