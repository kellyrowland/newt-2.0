from django.test import TestCase
from django.conf import settings
from django.urls import reverse
import json
import time
import os
from newt.tests import MyTestClient, login
from authnz import urls

try:
    from newt.local_settings import test_machine as machine
except ImportError:
    machine = "localhost"

class JobTests(TestCase):
    fixtures = ["test_fixture.json"]
    

    def setUp(self):
        self.client = MyTestClient()
        self.client.post(reverse('newt-auth'), data=login)

    def test_get_queues(self):
        # Tests getting queues
        r = self.client.get(reverse('newt-job'))
        self.assertEqual(r.status_code, 200)
        json_response = r.json()
        self.assertTrue(len(json_response['output']) > 0)
        self.assertIn(machine, list(json_response['output'].keys()))

    def test_running_cmds(self):

        # Tests submitting a job
        payload = {
            "jobscript": "/bin/hostname\nsleep 10"
        }
        r = self.client.post(reverse('newt-job-machine',
            args=(machine,)), data=payload)
        self.assertEqual(r.status_code, 200)
        json_response = r.json()
        self.assertIsNot(json_response['output']['jobid'], None)

        # Get job id from submitting the job
        job_id = json_response['output']['jobid']

        # Give the process time to register
        time.sleep(1)  

        # Tests getting job info
        r = self.client.get(reverse('newt-job-machine-jobid',args=(machine,job_id,)))
        self.assertEqual(r.status_code, 200)
        json_response = r.json()
        self.assertEqual(json_response['output']['jobid'], job_id)
        self.assertEqual(json_response['output']['user'], login['username'])
        
        # Delete job from queue
        r = self.client.get(reverse('newt-job-machine-jobid',args=(machine,job_id,)))
        self.assertEqual(r.status_code, 200)
