import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app, connect_to_db, createPhysician, deleteUser, deleteSchedule, getPhysiciansByIdUsingName


class TestScheduling(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Get the Flask test client
        cls.client = app.test_client()
        # Connect to database
        connect_to_db(app)

    def test_create_schedule(self):
        createPhysician('phy1', 'phy1', 'audrey', 'powers', '123 Street', 'Iowa City', 'Iowa', '319-883-9334', '99/99/9999', 's', '1', '1', '1', '1', '1', '1')
        response = self.client.post('/api/setHours', data=dict(
            physician='audrey powers',
            MondayTimes='02:00 PM-03:00 PM',
            TuesdayTimes='02:00 PM-03:00 PM',
            WednesdayTimes='',
            ThursdayTimes='',
            FridayTimes='',
            SaturdayTimes='',
            SundayTimes=''
        ))
        self.assertEqual('/setHours', response.location)
        self.assertEqual(302, response.status_code)
        deleteSchedule(getPhysiciansByIdUsingName('audrey powers'))
        deleteUser('phy1')


if __name__ == '__main__':
    unittest.main()
