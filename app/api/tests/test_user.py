from app.api.tests.base import BaseCase
from flask import json

class TestCreateUser(BaseCase):
    def testCreateUser(self):
        with self.client:
            response = self.client.post(
                '/api/v1/users/',
                data = json.dumps(dict(
                    username='prossie',
                    password='johnz')),
                content_type='application/json')

            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertEqual(data[response.message], 'User sucessfully created')