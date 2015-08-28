# tests/test_api.py
import os
import unittest
from datetime import date

from project import app, db
from project._config import basedir
from project.models import Task

TEST_DB = 'test.db'


class APITests(unittest.TestCase):

    """Docstring for APITests. Setup and Teardown."""
    # execute prior to each test
    def setup(self):
        """TODO: Docstring for setup.
        :returns: TODO

        """
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABSE_URI'] = 'sqlite:///' + \
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

    # Helper methods
    def add_tasks(self):
        """TODO: Docstring for add_task.
        :returns: TODO

        """
        db.session.add(
            Task(
                "Run around in circles",
                date(2015, 10, 22),
                10,
                date(2015, 10, 5),
                1,
                1
            )
        )
        db.session.commit()

        db.session.add(
            Task(
                "Purchase Real Python",
                date(2016, 2, 23),
                10,
                date(2016, 2, 7),
                1,
                1
            )
        )
        db.session.commit()

    # Tests
    def test_collection_endpoint_returns_correct_data(self):
        """TODO: Docstring for test_collection_endpoint_returns_correct_data.
        :returns: TODO

        """
        self.add_tasks()
        response = self.app.get('api/v1/tasks/', follow_redirects=True)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.mimetype, 'application/json')
        self.assertIn(b'Run around in circles', response.data)
        self.assertIn(b'Purchase Real Python', response.data)


if __name__ == "__main__":
    unittest.main()