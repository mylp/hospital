import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app, connect_to_db, deleteUser

import unittest


# MUST RUN TEST_SIGN.PY BEFORE RUNNING TEST_LOGIN.PY, will fix this dependency eventually

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Get the Flask test client
        cls.client = app.test_client()
        # Connect to database
        connect_to_db(app)


    def test_sendNotification_success(self):
        response = self.client.post('/api/billNotification', data=dict(
            idpatient="23",
            idPhys="21",
        ))
        self.assertEquals('/physicianHome', response.location)
        self.assertEquals(response.status_code, 200)

def test_sendNotification_fail(self):
        response = self.client.post('/api/billNotification', data=dict(
            idpatient="21",
            idPhys="21",
        ))
        self.assertEquals(None, response.location)
        self.assertEquals(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
