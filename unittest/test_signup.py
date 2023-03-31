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

    def test_signup_with_required_fields(self):
        response = self.client.post('/api/signup', data=dict(
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
        self.assertEquals(response.location, '/userHome')
        self.assertEquals(response.status_code, 302)
    
    def test_signup_with_missing_field(self):
        response = self.client.post('/api/signup', data=dict(
            inputFirst='John',
            inputLast='Doe',
            inputStreet='123 Main St',
            inputCity='Anytown',
            inputState='',
            inputZip='12345',
            inputPhone='555-123-4567',
            inputDOB='01/01/2000',
            inputSex='Male',
            inputEmail='john.doe@example.com',
            inputUsername='johndoe',
            inputPassword='password'
        ))
        self.assertEquals(response.location, None)
        self.assertEquals(response.status_code, 200)



if __name__ == '__main__':
    unittest.main()
