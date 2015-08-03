import json

from flask import request
from flask_restful import Resource, reqparse

from app import db, User
from app.lib.response_util import buildOkResponse
from app.lib import status


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
        if not('name' in request.form and 'email' in request.form and
            'password' in request.form):
            raise status.BadRequest('You need all three arguments: name, email, password')

        newUser = User(request.form.get('name'),
                       request.form.get('email'),
                       request.form.get('password'))
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

        user.name = request.form.get('name') or user.name
        user.password = request.form.get('password') or user.password

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
