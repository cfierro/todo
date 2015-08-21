from flask import request, session
from flask_restful import Resource

from app import db, TodoList, TodoListPermission
from app.lib import authentication, response_util, status


class TodoListMultiResource(Resource):
    """Class for creating and accessing lists.
    """
    @authentication.requiresAuth
    def get(self):
        """Method gets a list of logged in user's todoLists and returns them in
        an Ok response.
        """
        userId = session.get('userId')
        todoLists = TodoList.query.filter_by(creatorId=userId)

        return response_util.buildOkResponse([todoList.toDict()
                                              for todoList in todoLists])

    @authentication.requiresAuth
    def post(self):
        """Method creates a todoList and returns it in an Ok response.
        """
        if not(request.form.get('name')):
            raise status.BadRequest()

        todoList = TodoList(request.form.get('name'), session.get('userId'))
        db.session.add(todoList)
        db.session.commit()

        permission = TodoListPermission(session.get('userId'), todoList.id)
        db.session.add(permission)
        db.session.commit()

        return response_util.buildOkResponse(todoList.toDict())


class TodoListResource(Resource):
    """Class to get, update, or delete a single todoList.
    """
    @authentication.requiresAuth
    def put(self, todoListId):
        """Method that updates and returns a todoList in an Ok response.

        Args:
            listId - An integer, primary key that identifies the todo list.
        """
        todoList = TodoList.query.get(todoListId)

        if todoList is None:
            raise status.NotFound()
        if todoList.creatorId != session.get('userId'):
            raise status.Unauthorized()

        todoList.name = request.form.get('name') or todoList.name
        db.session.commit()

        return response_util.buildOkResponse(todoList.toDict())

    @authentication.requiresAuth
    def get(self, todoListId):
        """Method that gets and returns a todoList in an Ok response.

        Args:
            todoListId - An integer, primary key that identifies the todo list.
        """
        todoList = TodoList.query.get(todoListId)

        if todoList is None:
            raise status.NotFound()
        if todoList.creatorId != session.get('userId'):
            raise status.Unauthorized()

        return response_util.buildOkResponse(todoList.toDict())

    @authentication.requiresAuth
    def delete(self, todoListId):
        """Method that deletes a todoList and returns result None.

        Args:
            todoListId - An integer, primary key that identifies the todo list.
        """
        todoList = TodoList.query.get(todoListId)

        if todoList is None:
            raise status.NotFound()
        if todoList.creatorId != session.get('userId'):
            raise status.Unauthorized()

        db.session.delete(todoList)
        db.session.commit()

        return response_util.buildOkResponse(None)
