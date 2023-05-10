import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app, connect_to_db, deleteCUMessage

import unittest


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Get the Flask test client
        cls.client = app.test_client()
        # Connect to database
        connect_to_db(app)

    def test_sendmessage(self):
        response = self.client.post('/api/contacted', data=dict(
            fname='test',
            lname='test',
            email='test@test.com',
            message='test'
        ))
        deleteCUMessage('test','test','test@test.com', 'test')
        self.assertEqual(None, response.location)
        self.assertEqual(200, response.status_code)

    def test_sendmessage_bad_email(self):
        response = self.client.post('/api/contacted', data=dict(
            fname='test',
            lname='test',
            email='testtest.com',
            message='test'
        ))
        self.assertEqual(None, response.location)
        self.assertEqual(200, response.status_code)

if __name__ == '__main__':
    unittest.main()
