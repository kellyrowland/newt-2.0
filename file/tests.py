from django.test import TestCase
from django.conf import settings
import json
import os
import random
from newt.tests import MyTestClient, newt_base_url, login
try:
    from newt.local_settings import test_machine as machine
except ImportError:
    machine = "localhost"


class FileTests(TestCase):
    def setUp(self):
        self.client = MyTestClient()
        self.client.post(newt_base_url + "/auth", data=login)

    def test_root(self):
        r = self.client.get(newt_base_url+'/file')
        self.assertEqual(r.status_code, 200)
        json_response = r.json()
        self.assertEqual(json_response['status'], "OK")
        self.assertIn(machine, json_response['output'])
        
    def test_getdir(self):        
        r = self.client.get(newt_base_url+'/file/'+machine+"/")
        self.assertEqual(r.status_code, 200)

        json_response = r.json()
        self.assertEqual(json_response['status'], "OK")
        
        self.assertTrue(len(json_response['output']) >= 2)
        self.assertEqual(json_response['output'][0]['name'], ".")
        self.assertEqual(json_response['output'][1]['name'], "..")
        
    def test_uploadfile(self):
        rand_string = '%010x' % random.randrange(16**10)
        r = self.client.put(newt_base_url + "/file/"+machine+"/tmp/tmp_newt_2.txt", data=rand_string)
        self.assertEqual(r.status_code, 200)
        json_response = r.json()
        self.assertEqual(json_response['output']['location'], "/tmp/tmp_newt_2.txt")
        r = self.client.get(newt_base_url+'/file/'+machine+'/tmp/tmp_newt_2.txt?download=true')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(next(r.streaming_content), rand_string)
        try:
            os.remove("/tmp/tmp_newt_2.txt")
        except Exception:
            pass
