from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_restful import Api

# Define the WSGI application object.
app = Flask(__name__)

# Setup application configuration.
app.config.from_object('config')

# Define database object which is imported by models and controllers.
db = SQLAlchemy(app)

# Import all models here for easier importing.
from app.users.models import User
from app.todo_lists.models import TodoList
from app.todos.models import Todo
from app.users.resources import UserListResource, UserResource
from app.todos.resources import todoMultiResource, todoResource
from app.todo_list.resources import todoListMultiResource, todoListResource

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
