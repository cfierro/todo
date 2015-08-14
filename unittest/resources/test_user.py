import json

from app import db, User
from unittest import ResourceTest


class TestUser(ResourceTest):
    """Superclass for helper methods.
    """
    def mySetup(self):
        pass

    def myTeardown(self):
        pass


class TestUser_get(TestUser):
    """Test cases for the get API endpoint.
    """
    def test_get_success(self):
        """Verify user is successfully returned.
        """
        user = User('Test User', 'test@test.com', 'password')
        db.session.add(user)
        db.session.commit()
        resp = self.client.get('/users/%s' % user.id)

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

    def test_get_notFound(self):
        """Verify NotFound is raised when user with the given ID does not exist.
        """
        resp = self.client.get('/users/1000')

        assert resp.status_code == 404
        assert json.loads(resp.data) == {
            'info': {},
            'status': {
                'statusCode': 404,
                'statusMsg': 'Not found',
                'statusDetails': {}
            },
            'result': {}
        }

    def test_get_listSuccess(self):
        """Verify list of users is successfully returned.
        """
        user1 = User('Test1 User', 'test1@test.com', 'password1')
        user2 = User('Test2 User', 'test2@test.com', 'password2')
        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()
        resp = self.client.get('/users')

        assert resp.status_code == 200
        assert json.loads(resp.data) == {
            'info': {},
            'status': {
                'statusMsg': 'Ok',
                'statusDetails': {},
                'statusCode': 'HTTPOK'
            },
            'result': [
                {
                    'id': 1,
                    'name': 'Test1 User',
                    'email': 'test1@test.com'
                },
                {
                    'id': 2,
                    'name': 'Test2 User',
                    'email': 'test2@test.com'
                }
            ]
        }


class TestUser_post(TestUser):
    """Test resources for the API post endpoint.
    """
    def test_post_success(self):
        """Verify new user is successfully returned.
        """
        user = {
            'name': 'Test User',
            'email': 'test@test.com',
            'password': 'test'
            }

        resp = self.client.post('/users/', data=user)

        assert resp.status_code == 200
        assert json.loads(resp.data) == {
            'info': {},
            'status': {
                'statusCode': 'HTTPOK',
                'statusMsg': 'Ok',
                'statusDetails': {}
            },
            'result': {
                'id': 1,
                'name': 'Test User',
                'email': 'test@test.com'
            }
        }

    def test_post_badRequest(self):
        """Verify BadRequest is raised when user fields are missing.
        """
        user = {}

        resp = self.client.post('/users/', data=user)

        assert resp.status_code == 400
        assert json.loads(resp.data) == {
            'info': {},
            'status': {
                'statusCode': 400,
                'statusMsg': 'Bad request',
                'statusDetails': {}
            },
            'result': {}
        }


class TestUser_put(TestUser):
    """Test resources for the API put endpoint.
    """
    def test_put_success(self):
        """Verify updated user is successfully returned.
        """
        user = User('Test User', 'test@test.com', 'password')
        db.session.add(user)
        db.session.commit()

        newUserData = {
            'name': 'Updated User',
            'password': 'updatedpass'
        }

        resp = self.client.put('/users/%s' % user.id, data=newUserData)

        assert resp.status_code == 200
        assert json.loads(resp.data) == {
            'info': {},
            'status': {
                'statusCode': 'HTTPOK',
                'statusMsg': 'Ok',
                'statusDetails': {}
            },
            'result': {
                'id': 1,
                'name': 'Updated User',
                'email': 'test@test.com'
            }
        }

    def test_put_notFound(self):
        """Verify NotFound is raised when user with the given ID does not exist.
        """
        resp = self.client.put('/users/1000')

        assert resp.status_code == 404
        assert json.loads(resp.data) == {
            'info': {},
            'status': {
                'statusCode': 404,
                'statusMsg': 'Not found',
                'statusDetails': {}
            },
            'result': {}
        }


class TestUser_delete(TestUser):
    """Test resources for the API put endpoint.
    """
    def test_delete_success(self):
        """Verify user is successfully deleted.
        """
        user = User('Test User', 'test@test.com', 'password')
        db.session.add(user)
        db.session.commit()

        resp = self.client.delete('/users/%s' % user.id)

        assert resp.status_code == 200
        assert json.loads(resp.data) == {
            'info': {},
            'status': {
                'statusCode': 'HTTPOK',
                'statusMsg': 'Ok',
                'statusDetails': {}
            },
            'result': None
        }

    def test_delete_notFound(self):
        """Verify NotFound is raised when user with the given ID does not exist.
        """
        resp = self.client.delete('/users/1000')

        assert resp.status_code == 404
        assert json.loads(resp.data) == {
            'info': {},
            'status': {
                'statusCode': 404,
                'statusMsg': 'Not found',
                'statusDetails': {}
            },
            'result': {}
        }
