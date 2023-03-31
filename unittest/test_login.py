import unittest
import os
import sys
from flask import url_for
from flask_testing import TestCase

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app



class TestSignUp(TestCase):

    def create_app(self):
        return app

    def test_login_with_correct_credentials(self):
        response = self.client.post('/api/validateLogin', data=dict(
            inputUsername='johndoe',
            inputPassword='password',
        ))
        self.assertEquals(response.location, '/userHome')
        self.assertEquals(response.status_code, 302)

    def test_login_with_incorrect_credentials(self):
        response = self.client.post('/api/validateLogin', data=dict(
            inputUsername='johndoe',
            inputPassword='wrongpassword',
        ))
        self.assertEquals(response.location, None)
        self.assertEquals(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
