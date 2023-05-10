import unittest
from app import app, connect_to_db, createStatement, createInvoice, deleteStatement, deleteInvoice, getStatementId, deletePaymentHistory


class TestPayment(unittest.TestCase):

    def test_make_payment(self):
        with app.test_client() as testing_client:
            connect_to_db(app)
            with testing_client.session_transaction() as s:
                s['user'] = '100'
        statementID = int(createStatement(100, 2000, "0000-00-0")[0][0])
        createInvoice(statementID, 2000, 100, 1900, 'testing payment')

        response = testing_client.post('/makePayment', data=dict(
            statementID=statementID,
            amount=100
        ))
        deletePaymentHistory(statementID, '100')
        deleteInvoice(statementID)
        deleteStatement(statementID, '100')

        self.assertEqual(None, response.location)
        self.assertEqual(200, response.status_code)
