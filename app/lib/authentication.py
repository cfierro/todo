from functools import wraps

from flask import session

from app.lib import status


def requiresAuth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'userId' not in session:
            raise status.Unauthorized()
        return f(*args, **kwargs)
    return decorated
