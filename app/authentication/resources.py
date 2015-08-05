from flask import session
from flask_restful import Resource

from app.users.models import User
from app.lib.response_util import buildOkResponse, _returnUser


class UserLogin(Resource):
    """Class for logging in a user.
    """
    def get(self, userId):
        user = User.query.get(userId)
        session['id'] = user.id

        return buildOkResponse(_returnUser(user))

    def post(self, userId):
        return self.get(userId)


class UserLogOut(Resource):
    """Class for logging out a user.
    """
    def get(self):
        session.pop('id', None)

        return buildOkResponse(None)


class UserInfo(Resource):
    """Class for accessing logged in user information.
    """
    def get(self):

        if 'id' in session:
            userId = session['id']
            user = User.query.get(userId)
            return buildOkResponse(_returnUser(user))
        else:
            return buildOkResponse(None)
