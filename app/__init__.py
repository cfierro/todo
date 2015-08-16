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
Base = db.make_declarative_base()

# Import all models here for easier importing.
from app.users.models import User
from app.todo_lists.models import TodoList
from app.todos.models import Todo

# db.drop_all()
# db.create_all()

### Setup API endpoints ###

# Define api object.
api = Api(app)

# All resources that need to be routed should be routed here.

# Users API
from app.users.resources import UserListResource, UserResource
api.add_resource(UserListResource, '/users', '/users/')
api.add_resource(UserResource, '/users/<int:userId>', '/users/<int:userId>/')

# Todo API
from app.todos.resources import TodoMultiResource, TodoResource
api.add_resource(TodoMultiResource, '/todos', '/todos/')
api.add_resource(TodoResource, '/todos/<int:todoId>', '/todos/<int:todoId>/')

# TodoList API
from app.todo_lists.resources import TodoListMultiResource, TodoListResource
api.add_resource(TodoListMultiResource, '/todolists', '/todolists/')
api.add_resource(TodoListResource, '/todolists/<int:todoListId>',
                 '/todolists/<int:todoListId>/')

# Authentication API
from app.authentication.resources import UserLogin, UserLogOut, UserInfo
api.add_resource(UserLogin, '/login/<int:userId>', '/login/<int:userId>/')
api.add_resource(UserLogOut, '/logout', '/logout/')
api.add_resource(UserInfo, '/me', '/me/')

