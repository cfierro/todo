import json

from flask import request
from flask_restful import Resource

from app import db, User


def returnUser(user):
    """Private method to convert a user model into a dictionary."""

    return {
        "id": user.id, "name": user.name
    }


class UserListResource(Resource):
    """Class for creating and accessging users."""
    def get(self):
        """This method gets a list of all the users.
            Args:
            None.

            Returns:
            This method returns a dictionary containing a list of dictionaries of each user id and name.
        """
        users = User.query.all()
        return {
                'info': None,
                'status': {
                    'statusMsg': 'Ok',
                    'statusDetails': {},
                    'statusCode': None
                },
                'result': [{'id': user.id, 'name': user.name} for user in users]
            }


    def post(self):
        """This method adds a new user.
            Args:
            None.

            Returns:
            This method returns a dictionary with the id and name of the new user.
        """
        newUserData = json.loads(request.form['data'])  # this is a dictionary
        newUser = User(newUserData.get('name'), newUserData.get('email'), newUserData.get('password'))
        db.session.add(newUser)
        db.session.commit()

        result = returnUser(newUser)

        return {
                'info': None,
                'status': {
                    'statusMsg': 'Ok',
                    'statusDetails': {},
                    'statusCode': None
                },
                'result': result
            }


class UserResource(Resource):
    """Class to update or delete users."""
    def put(self, userId):
        """This method updates user information.
            Args:
            userId - An integer, primary key that identifies the user.

            Returns:
            This method returns a dictionary with the statusMsg "Ok" if successful.
        """
        user = User.query.get(userId)
        userData = json.loads(request.form['data'])

        user.name = userData.get('name') or user.name
        user.password = userData.get('password') or user.password

        db.session.commit()

        result = returnUser(user)

        return {
                'info': None,
                'status': {
                    'statusMsg': 'Ok',
                    'statusDetails': {},
                    'statusCode': None
                },
                'result': result
            }


# singular get
# Delete
#
