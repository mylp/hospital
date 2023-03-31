import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app

class Test(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_(self):
        response = self.app.post('/api/route', data=dict(
            inputFirst='John',
        ))
        self.assertEqual(response.status_code, 302)  # redirect to /userHome

if __name__ == '__main__':
    unittest.main()
