import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app, connect_to_db, deleteUser

import unittest


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Get the Flask test client
        cls.client = app.test_client()
        # Connect to database
        connect_to_db(app)

    def test_login_with_correct_credentials_user(self):
        self.client.post('/api/signup', data=dict(
            inputUsername='audrey',
            inputPassword='audrey!W22222',
            inputFirst='John',
            inputLast='Doe',
            inputStreet='123 Main St',
            inputCity='Anytown',
            inputState='CA',
            inputZip='12345',
            inputPhone='555-123-4567',
            inputDOB='01/01/2000',
            inputSex='M',
            inputEmail='john.doe@example.com'
        ))
        response = self.client.post('/api/validateLogin', data=dict(
            inputUsername='audrey',
            inputPassword='audrey!W22222',
        ))
        deleteUser('audrey')
        self.assertEqual('/userHome', response.location)
        self.assertEqual(302, response.status_code)

    def test_login_with_correct_credentials_admin(self):
        self.client.post('/api/signupAdmin', data=dict(
            inputUsername='admin1',
            inputPassword='admin1!222222W',
            inputFirst='John',
            inputLast='Doe',
            inputStreet='123 Main St',
            inputCity='Anytown',
            inputState='CA',
            inputZip='12345',
            inputPhone='555-123-4567',
            inputDOB='01/01/2000',
            inputSex='M',
            inputEmail='john.doe@example.com',
            inputDept=9
        ))
        response = self.client.post('/api/validateLogin', data=dict(
            inputUsername='admin1',
            inputPassword='admin1!222222W',
        ))
        deleteUser('admin1')
        self.assertEqual('/adminHome', response.location)
        self.assertEqual(302, response.status_code)

    def test_login_with_correct_credentials_physician(self):
        self.client.post('/api/signupPhysician', data=dict(
            inputUsername='physician',
            inputPassword='physician!W22222',
            inputFirst='John',
            inputLast='Doe',
            inputStreet='123 Main St',
            inputCity='Anytown',
            inputState='CA',
            inputZip='12345',
            inputPhone='555-123-4567',
            inputDOB='01/01/2000',
            inputSex='M',
            inputEmail='john.doe@example.com',
            inputSpec='something',
            inputRank='two',
            inputDept='9',
            inputClinic='10'

        ))
        response = self.client.post('/api/validateLogin', data=dict(
            inputUsername='physician',
            inputPassword='physician!W22222',
        ))
        deleteUser('physician')
        self.assertEqual('/physicianHome', response.location)
        self.assertEqual(302, response.status_code)

    def test_login_with_correct_credentials_nurse(self):
        self.client.post('/api/signupNurse', data=dict(
            inputUsername='nurse',
            inputPassword='nurse!W22222',
            inputFirst='John',
            inputLast='Doe',
            inputStreet='123 Main St',
            inputCity='Anytown',
            inputState='CA',
            inputZip='12345',
            inputPhone='555-123-4567',
            inputDOB='01/01/2000',
            inputSex='M',
            inputEmail='john.doe@example.com',
            inputClassification='1',
            inputDept='1',
            inputClinic='1'

        ))
        response = self.client.post('/api/validateLogin', data=dict(
            inputUsername='nurse',
            inputPassword='nurse!W22222',
        ))
        deleteUser('nurse')
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
