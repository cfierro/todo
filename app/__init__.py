from flask import Flask, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from flask_restful import Api

### Setup app configurations. ###

# Define the WSGI application object.
app = Flask(__name__)

# Setup application configuration.
app.config.from_object('config')

# Setup error handlers.
from app.lib.status import TodoException


@app.errorhandler(TodoException)
def handleBaseException(error):
    response = jsonify(error.toDict())
    response.status_code = error.statusCode
    return response

### Setup database ###

# Define database object which is imported by models and controllers.
db = SQLAlchemy(app)

# Import all models here for easier importing.
from app.users.models import User
from app.todo_lists.models import TodoList
from app.todos.models import Todo

db.create_all()

### Setup API endpoints ###

# Define api object.
api = Api(app)

# All resources that need to be routed should be routed here.
from app.users.resources import UserListResource, UserResource
from app.authentication.resources import UserLogin, UserLogOut, UserInfo

api.add_resource(UserListResource, '/users', '/users/')
api.add_resource(UserResource, '/users/<int:userId>', '/users/<int:userId>/')
api.add_resource(UserLogin, '/login/<int:userId>', '/login/<int:userId>/')
api.add_resource(UserLogOut, '/logout', '/logout/')
api.add_resource(UserInfo, '/me', '/me/')
