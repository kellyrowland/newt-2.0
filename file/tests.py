from django.test import TestCase
from django.conf import settings
from django.urls import reverse
import json
import os
import random
from newt.tests import MyTestClient, login
from authnz import urls
try:
    from newt.local_settings import test_machine as machine
except ImportError:
    machine = "localhost"


class FileTests(TestCase):
    def setUp(self):
        self.client = MyTestClient()
        self.client.post(reverse('newt-auth'), data=login)

    def test_root(self):
        r = self.client.get(reverse('newt-file'))
        self.assertEqual(r.status_code, 200)
        json_response = r.json()
        self.assertEqual(json_response['status'], "OK")
        self.assertIn(machine, json_response['output'])
        
    def test_getdir(self):
        r = self.client.get(reverse('newt-file-machine', args=(machine,)))
        self.assertEqual(r.status_code, 200)

        json_response = r.json()
        self.assertEqual(json_response['status'], "OK")
        
        self.assertTrue(len(json_response['output']) >= 2)
        self.assertEqual(json_response['output'][0]['name'], ".")
        self.assertEqual(json_response['output'][1]['name'], "..")
        
    def test_uploadfile(self):
        rand_string = '%010x' % random.randrange(16**10)
        r = self.client.put(reverse('newt-file-machine-path',
            args=(machine,"/tmp/tmp_newt_2.txt",)), rand_string)
        self.assertEqual(r.status_code, 200)
        json_response = r.json()
        self.assertEqual(json_response['output']['location'], "/tmp/tmp_newt_2.txt")
        r = self.client.get(reverse('newt-file-machine-path',
            args=(machine,"/tmp/tmp_newt_2.txt",)), download=True)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(next(r.streaming_content).decode("utf-8"), rand_string)
        try:
            os.remove("/tmp/tmp_newt_2.txt")
        except Exception:
            pass
