# tests/test_api.py
import os
import unittest
from datetime import date

from project import app, db
from project._config import BASE_DIR
from project.models import Task

TEST_DB = 'test.db'


class APITests(unittest.TestCase):

    """Docstring for APITests. Setup and Teardown."""
    # execute prior to each test
    def setUp(self):
        """TODO: Docstring for setup.
        :returns: TODO

        """
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
            os.path.join(BASE_DIR, TEST_DB)
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

    def test_resource_endpoint_returns_correct_data(self):
        """TODO: Docstring for test_resource_endpoint_returns_correct_data.
        :returns: TODO

        """
        self.add_tasks()
        response = self.app.get('api/v1/tasks/2', follow_redirects=True)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.mimetype, 'application/json')
        self.assertIn(b'Purchase Real Python', response.data)
        self.assertIn(b'Run around in circles', response.data)

    def test_invalid_recource_endpoint_returns_error(self):
        """TODO: Docstring for test_invalid_recource_endpoint_returns_error.
        :returns: TODO

        """
        self.add_tasks()
        response = self.app.get('api/v1/tasks/209', follow_redirects=True)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.mimetype, 'application/json')
        self.assertIn(b'Element does not exist', response.data)


if __name__ == "__main__":
    unittest.main()
