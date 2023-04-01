import os
import sys

from werkzeug.security import generate_password_hash

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app, connect_to_db, session

import unittest


class TestWebApp(unittest.TestCase):
    def setUp(self):
        # Get the Flask test client
        self.client = app.test_client()
        # Show Flask errors that happen during tests
        app.config['TESTING'] = True
        # Connect to database
        connect_to_db(app)


    def test_login_with_correct_credentials_user(self):
        response = self.client.post('/api/validateLogin', data=dict(
            inputUsername='audrey',
            inputPassword='audrey',
        ))
        self.assertEqual('/userHome', response.location)
        self.assertEqual(302, response.status_code)

    def test_login_with_correct_credentials_admin(self):
        response = self.client.post('/api/validateLogin', data=dict(
            inputUsername='admin',
            inputPassword='admin',
        ))
        self.assertEqual('/adminHome', response.location)
        self.assertEqual(302, response.status_code)

    def test_login_with_correct_credentials_physician(self):
        response = self.client.post('/api/validateLogin', data=dict(
            inputUsername='physician',
            inputPassword='physician',
        ))
        self.assertEqual('/physicianHome', response.location)
        self.assertEqual(302, response.status_code)

    def test_login_with_correct_credentials_nurse(self):
        response = self.client.post('/api/validateLogin', data=dict(
            inputUsername='nurse',
            inputPassword='nurse',
        ))
        self.assertEqual('/nurseHome', response.location)
        self.assertEqual(302, response.status_code)

    def test_login_with_incorrect_credentials(self):
        response = self.client.post('/api/validateLogin', data=dict(
            inputUsername='admin',
            inputPassword='wrongpassword',
        ))
        self.assertEquals(None, response.location)
        self.assertEquals(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
