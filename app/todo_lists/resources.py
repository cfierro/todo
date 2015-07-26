import json

from flask import request
from flask_restful import Resource

from app import db, TodoList
from app.lib.response_util import buildOkResponse


def _returnTodoList(todoList):
    """Private method to convert a todoList object into a dictionary.
    """
    return {
        "id": todoList.id,
        "name": todoList.name
    }


class TodoListMultiResource(Resource):
    """Class for creating and accessing lists.
    """
    def get(self):
        """Method gets a list of todoLists and returns them in an Ok response.
        """
        todoLists = TodoList.query.all()

        return buildOkResponse([_returnTodoList(todoList) for todoList in
                               todoLists])

    def post(self):
        """Method creates a todoList and returns it in an Ok response.
        """
        newListData = json.loads(request.form['data'])
        newList = TodoList(newListData['name'], newListData['userId'])

        db.session.add(newList)
        db.session.commit()

        return buildOkResponse(_returnTodoList(newList))


class TodoListResource(Resource):
    """Class to get, update, or delete a single todoList.
    """
    def put(self, listId):
        """Method that updates and returns a todoList in an Ok response.
        """
        todoList = TodoList.query.get(listId)
        todoListData = json.loads(request.form['data'])

        todoList.name = todoListData.get('name') or todoList.name
        todoList.userId = todoListData.get('userId') or todoList.userId

        db.session.update()

        return buildOkResponse(_returnTodoList(todoList))

    def get(self, listId):
        """Method that gets and returns a todoList in an Ok response.
        """
        todoList = TodoList.query.get(listId)
        return buildOkResponse(_returnTodoList(todoList))

    def delete(self, listId):
        """Method that deletes a todoList and returns result None.
        """
        todoList = TodoList.query.get(listId)
        db.session.delete(todoList)
        db.session.commit()

        return buildOkResponse(None)
