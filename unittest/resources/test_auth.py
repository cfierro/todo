import json

from flask import session

from app import db, User
from unittest import ResourceTest


class TestAuth(ResourceTest):
    """Superclass for helper methods.
    """
    def mySetup(self):
        pass

    def myTeardown(self):
        pass

class TestAuth_get(TestAuth):
    """Test cases for the get API endpoint.
    """
    def test_login_get_success(self):
        """Test user is successfully logged in.
        """
        user = User('Test User', 'test@test.com', 'password')
        db.session.add(user)
        db.session.commit()

        resp = self.client.get('/login/%s' % user.id)

        assert resp.status_code == 200
        assert json.loads(resp.data) == {
            'info': None,
            'status': {
                'statusMsg': 'Ok',
                'statusDetails': {},
                'statusCode': 'HTTPOK'
            },
            'result': {
                'id': 1,
                'name': 'Test User',
                'email': 'test@test.com'
            }
        }
