import json

from flask import request
from flask_restful import Resource

from app import db, TodoList
from app.lib import response_util, status


class TodoListMultiResource(Resource):
    """Class for creating and accessing lists.
    """
    def get(self):
        """Method gets a list of todoLists and returns them in an Ok response.
        """
        todoLists = TodoList.query.all()

        return response_util.buildOkResponse([todoList.toDict()
                                              for todoList in todoLists])

    def post(self):
        """Method creates a todoList and returns it in an Ok response.
        """
        if not(request.form.get('name') and request.form.get('creatorId')):
            raise status.BadRequest()

        todoList = TodoList(request.form.get('name'),
                            request.form.get('creatorId'))

        db.session.add(todoList)
        db.session.commit()

        return response_util.buildOkResponse(todoList.toDict())


class TodoListResource(Resource):
    """Class to get, update, or delete a single todoList.
    """
    def put(self, todoListId):
        """Method that updates and returns a todoList in an Ok response.

        Args:
            listId - An integer, primary key that identifies the todo list.
        """
        todoList = TodoList.query.get(todoListId)

        if todoList is None:
            raise status.NotFound()

        todoList.name = request.form.get('name') or todoList.name
        todoList.userId = request.form.get('creatorId') or todoList.creatorId

        db.session.commit()

        return response_util.buildOkResponse(todoList.toDict())

    def get(self, todoListId):
        """Method that gets and returns a todoList in an Ok response.

        Args:
            todoListId - An integer, primary key that identifies the todo list.
        """
        todoList = TodoList.query.get(todoListId)

        if todoList is None:
            raise status.NotFound()
        return response_util.buildOkResponse(todoList.toDict())

    def delete(self, todoListId):
        """Method that deletes a todoList and returns result None.

        Args:
            todoListId - An integer, primary key that identifies the todo list.
        """
        todoList = TodoList.query.get(todoListId)

        if todoList is None:
            raise status.NotFound()
        db.session.delete(todoList)
        db.session.commit()

        return response_util.buildOkResponse(None)
