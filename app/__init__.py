from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

# Define the WSGI application object.
app = Flask(__name__)

# Setup application configuration.
app.config.from_object('config')

# Define database object which is imported by models and controllers.
db = SQLAlchemy(app)

# Import all models here for easier importing.
from app.users.models import User
