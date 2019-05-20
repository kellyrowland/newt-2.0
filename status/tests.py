from django.test import TestCase
from django.conf import settings
from django.urls import reverse
import json
from newt.tests import MyTestClient


class StatusTests(TestCase):
    def setUp(self):
        self.client = MyTestClient()

    def test_all(self):
        r = self.client.get(reverse('newt-status'))
        self.assertEqual(r.status_code, 200)

        json_response = r.json()
        self.assertEqual(json_response['status'], "OK")

        for x in json_response['output']:
            if x['system'] == "localhost":
                self.assertEqual(x['status'], 'up')
            else:
                self.assertIn(x['status'], ['up', 'down'])

    def test_one(self):
        system = settings.NEWT_CONFIG['SYSTEMS'][0]['NAME']
        r = self.client.get(reverse('newt-status-machine',args=(system,)))
        self.assertEqual(r.status_code, 200)

        json_response = r.json()
        self.assertEqual(json_response['status'], "OK")

        self.assertEqual(json_response['output']['status'], 'up')