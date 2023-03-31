import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app

class TestSignUp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_signup_with_required_fields(self):
        response = self.app.post('/api/signup', data=dict(
            inputFirst='John',
            inputLast='Doe',
            inputStreet='123 Main St',
            inputCity='Anytown',
            inputState='CA',
            inputZip='12345',
            inputPhone='555-123-4567',
            inputDOB='01/01/2000',
            inputSex='Male',
            inputEmail='john.doe@example.com',
            inputUsername='johndoe',
            inputPassword='password'
        ))
        self.assertEqual(response.status_code, 302)  # redirect to /userHome

    def test_signup_with_missing_fields(self):
        response = self.app.post('/api/signup', data=dict(
            inputFirst='John',
            inputLast='Doe',
            inputStreet='',
            inputCity='Anytown',
            inputState='CA',
            inputZip='12345',
            inputPhone='555-123-4567',
            inputDOB='01/01/2000',
            inputSex='Male',
            inputEmail='john.doe@example.com',
            inputUsername='johndoe',
            inputPassword='password'
        ))
        self.assertEqual(response.status_code, 200)  # return error message

if __name__ == '__main__':
    unittest.main()
