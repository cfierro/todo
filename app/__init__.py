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

api = Api(app)

# All resources that need to be routed should be routed here.
api.add_resource(UserListResource, '/users', '/users/')
api.add_resource(UserResource, '/users/<int:userId>', '/users/<int:userId>/')

db.create_all()
