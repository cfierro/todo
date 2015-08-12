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
    def test_something(self):
        """Sample test.
        """
        user = User('Test User', 'test@test.com', 'password')
        db.session.add(user)
        db.session.commit()
        resp = self.client.get('/users/%s' % user.id)

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
