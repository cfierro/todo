import json

from flask import request
from flask_restful import Resource

from app import db, User
from app.lib.response_util import buildOkResponse


def returnUser(user):
    """Private method to convert a user model into a dictionary.

        Args:
        user: A user model.
    """

    return {
        "id": user.id, "name": user.name
    }


class UserListResource(Resource):
    """Class for creating and accessging users."""
    def get(self):
        """
            This method gets a list of all the users.

            Returns:
            Method returns the a list of user names and ids in dictionary
            format.
        """
        users = User.query.all()
        return buildOkResponse([returnUser(user) for user in users])

    def post(self):
        """This method adds a new user.

            Returns:
            Method returns the new user name and id in dictionary format.
        """
        newUserData = json.loads(request.form['data'])  # this is a dictionary
        newUser = User(newUserData.get('name'), newUserData.get('email'),
                       newUserData.get('password'))
        db.session.add(newUser)
        db.session.commit()

        return buildOkResponse(returnUser(newUser))


class UserResource(Resource):
    """Class to update, get, or delete users."""
    def put(self, userId):
        """This method updates user information.
            Args:
            userId - An integer, primary key that identifies the user.

            Returns:
            Method returns the updated user name and id in dictionary format.
        """
        user = User.query.get(userId)
        userData = json.loads(request.form['data'])

        user.name = userData.get('name') or user.name
        user.password = userData.get('password') or user.password

        db.session.commit()

        return buildOkResponse(returnUser(user))

    def get(self, userId):
        """This method gets a single user.
            Args:
            userId - An integer, primary key that identifies the user.

            Returns:
            Method returns the user name and id in dictionary format.
        """

        user = User.query.get(userId)
        return buildOkResponse(returnUser(user))

    def delete(self, userId):
        """This method deletes a user.
            Args:
            userId - An integer, primary key that identifies the user.

            Returns:
            Method returns result none.
        """

        user = User.query.get(userId)
        db.session.delete(user)
        db.commit()

        return buildOkResponse(None)
