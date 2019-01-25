"""File for User Tests"""

import unittest
from app.models.user import User
from app import initialise_app
from db import DataBaseConnection
import json


# class TestUser(unittest.TestCase):
#     '''Class to test User routes'''
#     def setUp(self):
#         app = initialise_app()
#         self.test_client = app.test_client()
#         self.db = DataBaseConnection()
#         self.db.cur.execute("TRUNCATE TABLE interventions;")
#         self.db.test_create_incident()

    # def test_save_redflag(self):
    #     '''Function to test create a Red-Flag Test'''
    #     redflag1 = {
    #         "images": "images",
    #         "videos": "videos",
    #         "comment": "Lorem Ipsum is simply dummy text of the century.",
    #         "location": "Kampala",
    #         "status": "draft",
    #         "type": "RedFlag"
    #     }
    #     response = self.test_client.post(
    #         'api/v1/red-flags',
    #         json=redflag1)
    #     self.assertEqual(response.status_code, 201)

    # def test_signup_user(self):
    #     '''Function to test get all Red-Flags'''

    #     response = self.test_client.get('api/v1/red-flags')
    #     data = json.loads(response.data)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(data['status'], 200)
    #     self. assertEqual(data['data'][0]['redflagid'], 11)

    # def test_missing_save_redflag(self):
    #     '''Post a Red-Flag Test while missing 2 parameters; images and videos'''
    #     redflag2 = {
    #         "comment": "Lorem Ipsum is simply dummy text of the century.",
    #         "id": 0,
    #         "location": "Kampala",
    #         "status": "draft",
    #         "type": "RedFlag"
    #     }
    #     reponse = self.test_client.post(
    #         'api/v1/red-flags',
    #         json=redflag2
    #     )
    #     self.assertEqual(reponse.status_code, 400)

    # def test_none_save_redflag(self):
    #     '''Post a Red-Flag test with empty input'''
    #     redflag3 = {}
    #     reponse = self.test_client.post(
    #         'api/v1/red-flags',
    #         json=redflag3
    #     )
    #     self.assertEqual(reponse.status_code, 400)

    # def test_spec_redflag(self):
    #     '''Function to test getting a specific Red-Flag'''
    #     response = self.test_client.get('api/v1/red-flags/11')
    #     data = json.loads(response.data)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(data['status'], 200)
    #     self.assertEqual(data['data']['redflagid'], 11)
    #     self.assertEqual(data['data']['location'], "katakwi")

    # def test_del_redflag(self):
    #     '''Function to test delete a Red-Flag'''
    #     response = self.test_client.delete("/api/v1/red-flags/12")
    #     data = json.loads(response.data)
    #     self.assertEqual(response.status_code, 200)

    # def test_edit_redflag(self):
    #     '''Edit a Red-Flag Test'''
    #     redflag = {
    #         "images": "Images",
    #         "videos": "Videos",
    #         "comment": "Lorem Ipsum is simply dummy text of the century.",
    #         "created_by": "Patrick Kikomeko",
    #         "created_on": "21/12/18",
    #         "id": 0,
    #         "location": "Kampala",
    #         "status": "draft",
    #         "type": "RedFlag"
    #     }
    #     self.test_client.post('api/v1/red-flags', json=redflag)
    #     redflag1 = {
    #         "images": "Images1",
    #         "videos": "Videos1",
    #         "comment": "LALALALALALALALALALALAL.",
    #         "created_by": "Patrick Kikomeko",
    #         "created_on": "21/12/18",
    #         "id": 0,
    #         "location": "Kyambogo",
    #         "status": "draft",
    #         "type": "RedFlag"
    #     }
    #     response = self.test_client.patch("/api/v1/red-flags/0", json=redflag1)
    #     data = json.loads(response.data)
    #     self.assertEqual(response.status_code, 201)