import unittest
import os
import sys
from flask import url_for
from flask_testing import TestCase

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app



class TestAppointment(TestCase):

    def create_app(self):
        return app

    def test_appointment_create(self):
        pass

    def test_appointment_modify(self):
        pass

    def test_appointment_delete(self):
        pass


if __name__ == '__main__':
    unittest.main()
