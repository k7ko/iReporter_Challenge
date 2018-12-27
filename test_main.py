import unittest
from main import app, all_redflags, save_redflag
from models import Incident
import json

class TestRedflag(unittest.TestCase):
    def setUp(self):
        self.test_client = app.test_client()

    def test_all_redflag(self):
        redflag = {
            "Images": "Images",
            "Videos": "Videos",
            "comment": "Lorem Ipsum is simply dummy text of the century.",
            "createdBy": "Patrick Kikomeko",
            "createdOn": "21/12/18",
            "id": 2,
            "location": "Kampala",
            "status": "draft",
            "type": "RedFlag"
        }
        self.test_client.post('api/v1/red-flags', json = redflag)

        response = self.test_client.get('api/v1/red-flags')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data['data']), 1)
        

    def test_save_redflag(self):
        redflag1 = {
        "Images": "Images",
        "Videos": "Videos",
        "comment": "Lorem Ipsum is simply dummy text of the century.",
        "createdBy": "Patrick Kikomeko",
        "createdOn": "21/12/18",
        "id": 2,
        "location": "Kampala",
        "status": "draft",
        "type": "RedFlag"
        }
        response = self.test_client.post(
            'api/v1/red-flags',
            json = redflag1)
        self.assertEqual(response.status_code, 201)

    def test_missing_save_redflag(self):
        #Missing 2 parameters; images and videos
        redflag2 = {
        "comment": "Lorem Ipsum is simply dummy text of the century.",
        "createdBy": "Patrick Kikomeko",
        "createdOn": "21/12/18",
        "id": 2,
        "location": "Kampala",
        "status": "draft",
        "type": "RedFlag"
        }
        reponse = self.test_client.post(
            'api/v1/red-flags',
            json = redflag2
        )
        self.assertEqual(reponse.status_code, 400)

    def test_none_save_redflag(self):
        #Empty Input
        redflag3 = {}
        reponse = self.test_client.post(
            'api/v1/red-flags',
            json = redflag3
        )
        self.assertEqual(reponse.status_code, 400)
