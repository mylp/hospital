import unittest
import os
import sys
from flask import url_for
from flask_testing import TestCase

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app



class TestAppointment(TestCase):

    def bed_created(self):
        response = self.client.post('/api/ManageBeds', data=dict(
            idBede=1,
            idClinic=1,
            roomNum=1,
            status=1,
            idPatient=0,
            
        ))
        self.assertEquals(response.location, '/ManageBeds')
        self.assertEquals(response.status_code, 200)


    
    def bed_deleted(self):
        response = self.client.post('/api/ManageBeds', data=dict(
            idBede=1,          
        ))
        self.assertEquals(response.location, '/ManageBeds')
        self.assertEquals(response.status_code, 200)

        


if __name__ == '__main__':
    unittest.main()
