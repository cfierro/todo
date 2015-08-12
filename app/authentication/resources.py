from flask import session
from flask_restful import Resource


from app.users.models import User
from app.lib import authentication, response_util


class UserLogin(Resource):
    """Class for logging in a user.
    """
    def get(self, userId):
        """Method to get a user id and create a new session.
        """
        user = User.query.get(userId)
        session['userId'] = user.id

        return response_util.buildOkResponse(user.toDict())

    def post(self, userId):
        """Method to post a user id and create a new session.
        """
        return self.get(userId)


class UserLogOut(Resource):
    """Class for logging out a user.
    """
    def get(self):
        """Method to get a user id and end the user's session.
        """
        session.pop('userId', None)

        return response_util.buildOkResponse(None)


class UserInfo(Resource):
    """Class for accessing logged in user information.
    """
    @authentication.requiresAuth
    def get(self):
        """Method to get the user information of the user logged in.
        """
        userId = session['userId']
        user = User.query.get(userId)
        return response_util.buildOkResponse(user.toDict())
