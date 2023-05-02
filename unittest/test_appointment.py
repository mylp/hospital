import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app, connect_to_db, create_appointment, save_appointment, modify_appointment, delete_appointment

class TestAppointment(unittest.TestCase):

    def setUpClass(cls):
        cls.client = app.test_client()
        connect_to_db(app)

    def test_create_appointment(self):
        pass

    def test_save_appointment(self):
        pass

    def test_modify_appointment(self):
        pass

    def test_delete_appointment(self):
        pass


if __name__ == '__main__':
    unittest.main()
