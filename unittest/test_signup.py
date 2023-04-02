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
            inputSex='Male',
            inputEmail='john.doe@example.com',
            inputUsername='audrey',
            inputPassword='audrey'
        ))
        deleteUser('audrey')
        self.assertEqual('/userHome', response.location)
        self.assertEqual(302, response.status_code)

    def test_signup_with_required_fields_phys(self):
        response = self.client.post('/api/signupPhysician', data=dict(
            inputUsername='physician',
            inputPassword='physician',
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
            Specialization='something',
            Rank='two',
            DepartmentID='9',
            ClinicID='10'

        ))
        deleteUser('physician')
        self.assertEqual('/adminHome', response.location)
        self.assertEqual(302, response.status_code)

    def test_signup_with_required_fields_nurse(self):
        response = self.client.post('/api/signupNurse', data=dict(
            inputUsername='nurse',
            inputPassword='nurse',
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
            Classification='1',
            DepartmentID='1',
            ClinicID='1'

        ))
        deleteUser('nurse')
        self.assertEqual('/adminHome', response.location)
        self.assertEqual(302, response.status_code)

    def test_signup_with_required_fields_admin(self):
        response = self.client.post('/api/signupAdmin', data=dict(
            inputUsername='admin1',
            inputPassword='admin1',
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
            Type='admin',
            DepartmentID=9
        ))
        deleteUser('admin1')
        self.assertEqual('/adminHome', response.location)
        self.assertEqual(302, response.status_code)

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
        self.assertEqual(None, response.location)
        self.assertEqual(200, response.status_code)


if __name__ == '__main__':
    unittest.main()
