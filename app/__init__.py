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
from app.users.resources import UserListResource, UserResource
from app.todos.resources import todoMultiResource, todoResource
from app.todo_list.resources import todoListMultiResource, todoListResource

db.create_all()

### Setup API endpoints ###

# Define api object.
api = Api(app)

# All resources that need to be routed should be routed here.
api.add_resource(UserListResource, '/users', '/users/')
api.add_resource(UserResource, '/users/<int:userId>', '/users/<int:userId>/')
api.add_resource(todoMultiResource, '/todos', '/todos/')
api.add_resource(todoResource, '/todos/<int:todoId>', 'todos/<int:todoId>/')
api.add_resource(todoListMultiResource, '/todolist', '/todolist/')
api.add_resource(todoListResource, '/todolist/<int:todoListId>',
                 '/todolist/<int:todoListId>/')

db.create_all()

