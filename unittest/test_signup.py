import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app, connect_to_db, deleteUser


class TestSignUp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Get the Flask test client
        cls.client = app.test_client()
        # Connect to database
        connect_to_db(app)

    def test_signup_with_required_fields_user(self):
        response = self.client.post('/api/signup', data=dict(
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
            inputUsername='audrey',
            inputPassword='audrey!W222222'
        ))
        deleteUser('audrey')
        self.assertEqual('/userHome', response.location)
        self.assertEqual(302, response.status_code)

    def test_signup_with_required_fields_use_error(self):
        response = self.client.post('/api/signup', data=dict(
            inputFirst='John',
            inputLast='Doe',
            inputStreet='123 Main St',
            inputCity='Anytown',
            inputState='CA',
            inputZip='12345eeee',
            inputPhone='555-123-4567',
            inputDOB='01/01/2000',
            inputSex='M',
            inputEmail='john.doe@example.com',
            inputUsername='audrey',
            inputPassword='audrey!W222222'
        ))
        self.assertEqual(None, response.location)
        self.assertEqual(200, response.status_code)

    def test_signup_with_required_fields_phys(self):
        response = self.client.post('/api/signupPhysician', data=dict(
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
        deleteUser('physician')
        self.assertEqual('/adminHome', response.location)
        self.assertEqual(302, response.status_code)

    def test_signup_with_required_fields_phys_error(self):
        response = self.client.post('/api/signupPhysician', data=dict(
            inputUsername='physician',
            inputPassword='physician!W22222',
            inputFirst='John',
            inputLast='Doe',
            inputStreet='123 Main St',
            inputCity='Anytown',
            inputState='CA',
            inputZip='12345',
            inputPhone='5552-123-456722',
            inputDOB='01/01/2000',
            inputSex='M',
            inputEmail='john.doe@example.com',
            inputSpec='something',
            inputRank='two',
            inputDept='9',
            inputClinic='10'

        ))
        self.assertEqual(None, response.location)
        self.assertEqual(200, response.status_code)

    def test_signup_with_required_fields_nurse(self):
        response = self.client.post('/api/signupNurse', data=dict(
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
        deleteUser('nurse')
        self.assertEqual('/adminHome', response.location)
        self.assertEqual(302, response.status_code)

    def test_signup_with_required_fields_nurse_error(self):
        response = self.client.post('/api/signupNurse', data=dict(
            inputUsername='nurse',
            inputPassword='nurse!W22222',
            inputFirst='John',
            inputLast='Doe',
            inputStreet='123 Main St',
            inputCity='Anytown',
            inputState='CA',
            inputZip='12345',
            inputPhone='555-123-4567',
            inputDOB='01/0122/2000',
            inputSex='M',
            inputEmail='john.doe@example.com',
            inputClassification='1',
            inputDept='1',
            inputClinic='1'

        ))
        self.assertEqual(None, response.location)
        self.assertEqual(200, response.status_code)

    def test_signup_with_required_fields_admin(self):
        response = self.client.post('/api/signupAdmin', data=dict(
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
        deleteUser('admin1')
        self.assertEqual('/adminHome', response.location)
        self.assertEqual(302, response.status_code)

    def test_signup_with_required_fields_admin(self):
        response = self.client.post('/api/signupAdmin', data=dict(
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
            inputSex='Y',
            inputEmail='john.doe@example.com',
            inputDept=9
        ))
        self.assertEqual(None, response.location)
        self.assertEqual(200, response.status_code)

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
            inputPassword='password!W22222'
        ))
        deleteUser('johndoe')
        self.assertEqual(None, response.location)
        self.assertEqual(200, response.status_code)


if __name__ == '__main__':
    unittest.main()
