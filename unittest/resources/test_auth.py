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
    def test_loginGetSuccess(self):
        """Verify user is successfully logged in.
        """
        user = User('Test User', 'test@test.com', 'password')
        db.session.add(user)
        db.session.commit()

        resp = self.client.get('/login/%s' % user.id)

        assert resp.status_code == 200
        assert json.loads(resp.data) == {
            'info': {},
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

    def test_logoutGetSuccess(self):
        """Verify user is successfully logged out.
        """
        user = User('Test User', 'test@test.com', 'password')
        db.session.add(user)
        db.session.commit()

        self.client.get('/login/%s' % user.id)
        resp = self.client.get('/logout')

        assert resp.status_code == 200
        assert json.loads(resp.data) == {
            'info': {},
            'status': {
                'statusMsg': 'Ok',
                'statusDetails': {},
                'statusCode': 'HTTPOK'
            },
            'result': None
        }

    def test_userInfoGetSuccess(self):
        user = User('Test User', 'test@test.com', 'password')
        db.session.add(user)
        db.session.commit()

        self.client.get('/login/%s' % user.id)
        resp = self.client.get('/me')

        assert resp.status_code == 200
        assert json.loads(resp.data) == {
            'info': {},
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


    def test_unauthorized(self):
        resp = self.client.get('/me')

        assert resp.status_code == 401
        assert json.loads(resp.data) == {
            'info': {},
            'status': {
                'statusMsg': 'Unauthorized request.',
                'statusDetails': {},
                'statusCode': 401
            },
            'result': {}
        }
