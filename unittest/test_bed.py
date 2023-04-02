import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app, connect_to_db


class TestAppointment(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Get the Flask test client
        cls.client = app.test_client()
        # Connect to database
        connect_to_db(app)

    def test_bed_created(self):
        response = self.client.post('/api/addBed', data=dict(
            idBed=1000000,
            idClinic=1,
            roomNum='1',
            status='testBed',
            idPatient=0,

        ))
        self.assertEqual('/ManageBeds', response.location)
        self.assertEqual(302, response.status_code)

    def test_bed_deleted(self):
        response = self.client.post('/api/deleteBed', data=dict(
            idBed=1000000,
        ))
        self.assertEqual('/ManageBeds', response.location)
        self.assertEqual(302, response.status_code)


if __name__ == '__main__':
    unittest.main()
