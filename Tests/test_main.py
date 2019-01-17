'''Red-Flags Tests file'''
import unittest
from Routes.main import app, save_redflag, all_redflags
from Routes.main import spec_redflag, del_redflag, edit_redflag
from Models.models import Incident
import json


class TestRedflag(unittest.TestCase):
    '''Class to test Red-Flag'''
    def setUp(self):
        self.test_client = app.test_client()

    def test_all_redflag(self):
        '''Get all Red-Flags test'''
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
        self.test_client.post('api/v1/red-flags', json=redflag)

        response = self.test_client.get('api/v1/red-flags')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data['data']), 1)

    def test_save_redflag(self):
        '''Post a Red-Flag Test'''
        redflag1 = {
            "Images": "Images",
            "Videos": "Videos",
            "comment": "Lorem Ipsum is simply dummy text of the century.",
            "createdBy": "Patrick Kikomeko",
            "createdOn": "21/12/18",
            "id": 0,
            "location": "Kampala",
            "status": "draft",
            "type": "RedFlag"
        }
        response = self.test_client.post(
            'api/v1/red-flags',
            json=redflag1)
        self.assertEqual(response.status_code, 201)

    def test_missing_save_redflag(self):
        '''Post a Red-Flag Test while missing 2 parameters; images and videos'''
        redflag2 = {
            "comment": "Lorem Ipsum is simply dummy text of the century.",
            "createdBy": "Patrick Kikomeko",
            "createdOn": "21/12/18",
            "id": 0,
            "location": "Kampala",
            "status": "draft",
            "type": "RedFlag"
        }
        reponse = self.test_client.post(
            'api/v1/red-flags',
            json=redflag2
        )
        self.assertEqual(reponse.status_code, 400)


    def test_none_save_redflag(self):
        '''Post a Red-Flag test with empty input'''
        redflag3 = {}
        reponse = self.test_client.post(
            'api/v1/red-flags',
            json=redflag3
        )
        self.assertEqual(reponse.status_code, 400)

    def test_spec_redflag(self):
        '''Get a specific Red-Flag Test'''
        redflag = {
            "Images": "Images",
            "Videos": "Videos",
            "comment": "Lorem Ipsum is simply dummy text of the century.",
            "createdBy": "Patrick Kikomeko",
            "createdOn": "21/12/18",
            "id": 0,
            "location": "Kampala",
            "status": "draft",
            "type": "RedFlag"
        }
        self.test_client.post('api/v1/red-flags', json=redflag)
        redflag = {
            "Images": "Images",
            "Videos": "Videos",
            "comment": "Lorem Ipsum is simply dummy text of the century.",
            "createdBy": "Patrick Kikomeko",
            "createdOn": "21/12/18",
            "id": 1,
            "location": "Kampala",
            "status": "draft",
            "type": "RedFlag"
        }
        self.test_client.post('api/v1/red-flags', json=redflag)
        response = self.test_client.get('api/v1/red-flags/0')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)


    def test_del_redflag(self):
        '''Delete a Red-Flag Test'''
        redflag = {
            "Images": "Images",
            "Videos": "Videos",
            "comment": "Lorem Ipsum is simply dummy text of the century.",
            "createdBy": "Patrick Kikomeko",
            "createdOn": "21/12/18",
            "id": 0,
            "location": "Kampala",
            "status": "draft",
            "type": "RedFlag"
        }
        self.test_client.post('api/v1/red-flags', json=redflag)
        response = self.test_client.delete("/api/v1/red-flags/0")
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)

    def test_edit_redflag(self):
        '''Edit a Red-Flag Test'''
        redflag = {
            "Images": "Images",
            "Videos": "Videos",
            "comment": "Lorem Ipsum is simply dummy text of the century.",
            "createdBy": "Patrick Kikomeko",
            "createdOn": "21/12/18",
            "id": 0,
            "location": "Kampala",
            "status": "draft",
            "type": "RedFlag"
        }
        self.test_client.post('api/v1/red-flags', json=redflag)
        redflag1 = {
            "Images": "Images1",
            "Videos": "Videos1",
            "comment": "LALALALALALALALALALALAL.",
            "createdBy": "Patrick Kikomeko",
            "createdOn": "21/12/18",
            "id": 0,
            "location": "Kyambogo",
            "status": "draft",
            "type": "RedFlag"
        }
        response = self.test_client.patch("/api/v1/red-flags/0", json=redflag1)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)