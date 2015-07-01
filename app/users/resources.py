from flask import request
from flask_restful import Resource
import json

from app.users.models import User
from app import db

class UserListResource(Resource):
    def get(self):
        users = User.query.all()
        return {
            'result': [{'id': user.id, 'name': user.name} for user in users]
            }

    def post(self):
        # import pdb; pdb.set_trace()
        new_user_data = json.loads(request.form['data'])  # this is a dictionary
        new_user = User(new_user_data.get('name'), new_user_data.get('email'), new_user_data.get('password'))
        db.session.add(new_user)
        db.session.commit()

        return {
                'result': {
                'id': new_user.id, 'name': new_user.name
                }
            }


class UserResource(Resource):
    def put(self, user_id):
        user = User.query.get(user_id)
        user_data = json.loads(request.form['data'])

        user.name = user_data.get('name') or user.name
        user.password = user_data.get('password') or user.password

        db.session.commit()

        return {
                'status': {
                    'statusMsg': "Ok"
                }
        }


# singular get
# Delete
#
