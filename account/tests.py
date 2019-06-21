from django.test import TestCase
from django.conf import settings
from django.urls import reverse
import json
from newt.tests import newt_base_url, MyTestClient, login

class AcctTests(TestCase):
    fixtures = ["test_fixture.json"]

    def setUp(self):
        self.client = MyTestClient()

    def test_info_ret(self):
        self.client.post(newt_base_url + "/auth/", data=login)

        r = self.client.get(reverse('newt-account-user-name', args=(login['username'],)))
        self.assertEqual(r.status_code, 200)
        json_response = r.json()
        self.assertEqual(json_response['output']['username'], login['username'])

        r = self.client.get(reverse('newt-account-user-id', args=(2,)))
        self.assertEqual(r.status_code, 200)
        json_response = r.json()
        self.assertEqual(json_response['output']['username'], login['username'])

        r = self.client.get(reverse('newt-account-group-id', args=(1,)))
        self.assertEqual(r.status_code, 200)
        json_response = r.json()
        self.assertEqual(json_response['output']['name'], "Test Group")
