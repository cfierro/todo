import os

from config import BASE_DIR
from app import app, db, User

class ResourceTest(object):
    """Superclass for all resource tests.
    """
    def setup_method(self, method):
        """Setup method called before every test.
        """
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = \
            'sqlite:///' + os.path.join(BASE_DIR, 'test.db')
        db.create_all()
        self.client = app.test_client()
        self.mySetup()

    def teardown_method(self, method):
        """Teardown method called after every test.
        """
        self.myTeardown()
        db.session.remove()
        db.drop_all()

    def mySetup(self):
        """To be overriden by the test class.
        """
        pass

    def myTeardown(self):
        """To be overriden by the test class.
        """
        pass
