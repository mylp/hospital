import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app


class TestScheduling(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_create_schedule_with_correct_fields(self):
        response = self.app.post('/api/setHours', data=dict(
            _mon=1,
            _tue=0,
            _wed=0,
            _thurs=0,
            _fri=0,
            _sat=0,
            _sun=0,
            _pid='1',
            _monTL='02:00 PM-06:00 PM',
            _tueTL='',
            _wedTL='',
            _thursTL='',
            _friTL='',
            _satTL='',
            _sunTL=''
        ))
        self.assertEquals(response.location, '/setHoursSuccess')
        self.assertEquals(response.status_code, 302)


if __name__ == '__main__':
    unittest.main()
