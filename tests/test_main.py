# project/test_main.py
import os
import unittest

from project import app, db
from project._config import basedir
from project.models import User

TEST_DB = 'test.db'


class MainTest(unittest.TestCase):

    """Docstring for MainTest. Setup and teardown"""
    # execute prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
            os.path.join(basedir, TEST_DB)
        self.app = app.test_client()
        db.create_all()
        self.assertEquals(app.debug, False)

    # execute after each test
    def tearDown(self):
        """TODO: Docstring for tearDown.
        :returns: TODO

        """
        db.session.remove()
        db.drop_all()

    # helper methods
    def login(self, name, password):
        """TODO: Docstring for login.
        :returns: TODO

        """
        return self.app.post('/', data=dict(
            name=name, password=password), follow_redirects=True)
        
    # tests
    def test_404_error(self):
        """TODO: Docstring for test_404_error.
        :returns: TODO

        """
        response = self.app.get('/this-route-does-not-exist/')
        self.assertEquals(response.status_code, 404)
        self.assertIn(b'Sorry. There\'s nothing here.', response.data)

if __name__ == "__main__":
    unittest.main()
