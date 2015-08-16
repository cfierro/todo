# Ask about getting branches up to date once committed

import json

from flask import request
from flask_restful import Resource

from app import db, Todo
from app.lib import response_util, status


class TodoMultiResource(Resource):
    """Class for creating and accessing todos.
    """
    def get(self):  # Should this take a user and return their todos?
        """Method gets a list of all the todos and returns them in an OK
        response.
        """
        todos = Todo.query.all()

        return response_util.buildOkResponse([todo.toDict() for todo in todos])

    def post(self):
        """Method adds a new todo.
        """
        if not(request.form.get('subject') and request.form.get('todoListId')):
            raise status.BadRequest()

        todo = Todo(request.form.get('subject'),
                    request.form.get('todoListId'),
                    request.form.get('dueDate'),
                    request.form.get('description'),
                    request.form.get('priority'),
                    request.form.get('completed'),
                    request.form.get('assigneeId'))
        db.session.add(todo)
        db.session.commit()

        return response_util.buildOkResponse(todo.toDict())


class TodoResource(Resource):
    """Class for updating, delelting, getting single todo.
    """
    def put(self, todoId):
        """Method updates a todo information and returns todo in an OK response.

        Args:
            todoId - Interger, primary key identifying the todo.
        """
        todo = Todo.query.get(todoId)

        if todo is None:
            raise status.NotFound()

        todo.subject = request.form.get('subject') or todo.subject
        todo.dueDate = request.form.get('dueDate') or todo.dueDate
        todo.description = request.form.get('description') or todo.description
        todo.priority = request.form.get('priority') or todo.priority
        todo.completed = request.form.get('completed') or todo.completed
        todo.assigneeId = request.form.get('assigneeId') or todo.assigneeId

        db.session.commit()

        return response_util.buildOkResponse(todo.toDict())

    def get(self, todoId):
        """Method gets and returns a single todo in an OK response.

        Args:
            todoId - Interger, primary key identifying the todo.
        """
        todo = Todo.query.get(todoId)
        if todo is None:
            raise status.NotFound()
        return response_util.buildOkResponse(todo.toDict())

    def delete(self, todoId):
        """Method deletes a todo and returns result none.

        Args:
            todoId - Interger, primary key identifying the todo.
        """
        todo = Todo.query.get(todoId)
        if todo is None:
            raise status.NotFound()
        db.session.delete(todo)
        db.session.commit()

        return response_util.buildOkResponse(None)
