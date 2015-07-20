import json

from flask import request
from flask_restful import Resource

from app import db, User
from app.lib.response_util import buildOkResponse


def _returnUser(user):
    """Private method to convert a user model into a dictionary.

    Args:
        user - A user model.
    """
    return {
        "id": user.id,
        "name": user.name
    }


class UserListResource(Resource):
    """Class for creating and accessing users.
    """
    def get(self):
        """This method gets a list of all the users and returns them in
        an OK response.
        """
        users = User.query.all()
        return buildOkResponse([_returnUser(user) for user in users])

    def post(self):
        """This method adds a new user and returns the user in an OK response.
        """
        newUserData = json.loads(request.form['data'])  # this is a dictionary
        newUser = User(newUserData['name'], newUserData['email'],
                       newUserData['password'])
        db.session.add(newUser)
        db.session.commit()

        return buildOkResponse(_returnUser(newUser))


class UserResource(Resource):
    """Class to update, get, or delete users.
    """
    def put(self, userId):
        """This method updates user information and returns the user in an OK
        response.

        Args:
            userId - An integer, primary key that identifies the user.
        """
        user = User.query.get(userId)
        userData = json.loads(request.form['data'])

        user.name = userData.get('name') or user.name
        user.password = userData.get('password') or user.password

        db.session.commit()

        return buildOkResponse(_returnUser(user))

    def get(self, userId):
        """This method gets a single user and returns the user in an OK response.

        Args:
            userId - An integer, primary key that identifies the user.
        """
        user = User.query.get(userId)
        return buildOkResponse(_returnUser(user))

    def delete(self, userId):
        """This method deletes a user and returns result none.

        Args:
            userId - An integer, primary key that identifies the user.
        """
        user = User.query.get(userId)
        db.session.delete(user)
        db.commit()

        return buildOkResponse(None)
