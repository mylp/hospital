import unittest
import os
import sys
from flaskext.mysql import MySQL

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app, connect_to_db

class TestAppointment(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.client = app.test_client()
        connect_to_db(app)

    """     def test_create_appointment(self):
            with app.test_client() as client:
                with client.session_transaction() as session:
                    session['user'] = 1
                response = client.post('/api/createAppointment', data=dict(
                    inputDate='2022-02-02',
                    inputTime='12:00',
                    physician='p p',
                    inputReason='test'
                ))
                self.assertEqual(response.status_code,200)

    def test_save_appointment(self):
        response = self.client.post('/api/saveAppointment', data=dict(
            inputDate='2022-02-02',
            inputTime='10:30',
            physician='p p',
            inputReason='test',
            inputID='1'
        ))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, '/appointment') 
"""


    def test_modify_appointment(self):
        with self.client:
        # Set a value for session['user']
            with self.client.session_transaction() as session:
                session['user'] = 1  # Replace 1 with the user ID you want to use

            # Make a request to the modifyAppointment endpoint
            response = self.client.post('/api/createAppointment', data=dict(
                inputDate='2022-02-02',
                inputTime='10:00',
                physician='p p',
                patient='2',
                inputReason='test'
            ))
            self.assertEqual(response.status_code, 200)

            # Get the ID of the new appointment
            appointment_id = int(response.location.split("/")[-1])

            # Modify the appointment
            response = self.client.post(f'/api/modifyAppointment?appointment_id={appointment_id}', data=dict(
                inputID=appointment_id,
                inputDate='2022-02-02',
                inputTime='10:00:00',
                physician='2',
                inputReason='updated'
            ))
            self.assertEqual(response.status_code, 200)

            # Check that the appointment was actually modified
            response = self.client.get('/appointment')
            self.assertIn(b'2022-02-02 10:00:00', response.data)
            self.assertIn(b'Physician 2', response.data)
            self.assertIn(b'updated', response.data)

            # Delete the appointment
            response = self.client.post(f'/api/deleteAppointment?appointment_id={appointment_id}')
            self.assertEqual(response.status_code, 302)

    """         def test_delete_appointment(self):
            appointment_id = 1
            response = self.client.post(f'/api/deleteAppointment?appointment_id={appointment_id}')
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.location, '/appointment') 
"""



if __name__ == '__main__':
    unittest.main()
