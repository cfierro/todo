import json

from flask import request
from flask_restful import Resource

from app import db, User
from app.lib import response_util
from app.lib import status


class UserListResource(Resource):
    """Class for creating and accessing users.
    """
    def get(self):
        """This method gets a list of all the users and returns them in
        an OK response.
        """
        users = User.query.all()
        return response_util.buildOkResponse([user._returnUser() for user in users])

    def post(self):
        """This method adds a new user and returns the user in an OK response.
        """
        newUser = User(request.form.get('name'),
                       request.form.get('email'),
                       request.form.get('password'))
        db.session.add(newUser)
        db.session.commit()

        return response_util.buildOkResponse(newUser._returnUser())


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

        return response_util.buildOkResponse(user._returnUser())

    def get(self, userId):
        """This method gets a single user and returns the user in an OK response.

        Args:
            userId - An integer, primary key that identifies the user.
        """
        user = User.query.get(userId)
        return response_util.buildOkResponse(user._returnUser())

    def delete(self, userId):
        """This method deletes a user and returns result none.

        Args:
            userId - An integer, primary key that identifies the user.
        """
        user = User.query.get(userId)
        db.session.delete(user)
        db.commit()

        return response_util.buildOkResponse(None)
