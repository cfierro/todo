import json

from flask import session

from app import db, User
from unittest import ResourceTest


class TestAuth(ResourceTest):
    """Superclass for helper methods.
    """
    def mySetup(self):
        self.user = User('Test User', 'test@test.com', 'password')
        db.session.add(self.user)
        db.session.commit()

    def myTeardown(self):
        pass

class TestAuth_get(TestAuth):
    """Test cases for the get API endpoint.
    """
    def test_loginGetSuccess(self):
        """Verify user is successfully logged in.
        """
        resp = self.client.get('/login/%s' % self.user.id)

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
        self.client.get('/login/%s' % self.user.id)
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
        """Verify user info successfully returned for logged in user.
        """
        self.client.get('/login/%s' % self.user.id)
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
        """Verify unauthorized is raised when user not logged in.
        """
        resp = self.client.get('/me')

        assert resp.status_code == 401
        assert json.loads(resp.data) == {
            'info': {},
            'status': {
                'statusMsg': 'Unauthorized request',
                'statusDetails': {},
                'statusCode': 401
            },
            'result': {}
        }
