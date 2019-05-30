from django.test import TestCase
from django.conf import settings
from django.urls import reverse
import json
import os
from newt.tests import MyTestClient, newt_base_url, login
from authnz import urls
from unittest import skipIf
try:
    from newt.local_settings import test_machine as machine
except ImportError:
    machine = "localhost"

import logging
logger = logging.getLogger("newt." + __name__)

class CommandTests(TestCase):
    def setUp(self):
        self.client = MyTestClient()
        self.client.post(reverse('newt-auth'), data=login)

    def test_root(self):
        r = self.client.get(reverse('newt-command'))
        self.assertEqual(r.status_code, 200)
        json_response = r.json()
        self.assertEqual(json_response['status'], "OK")
        self.assertIn(machine, json_response['output'])

    def test_command(self):
        r = self.client.post(reverse('newt-command-machine',
            args=(machine,)), {'command': '/bin/hostname'})
        self.assertEqual(r.status_code, 200)
        json_response = r.json()
        self.assertEqual(json_response['status'], "OK")
        self.assertIsNotNone(json_response['output']['output'])
        self.assertEqual(json_response['output']['retcode'], 0)

    @skipIf(machine != "localhost", "Can't run ls on remote machine")
    def test_command_with_args(self):
        # Run ls in / 
        r = self.client.post(reverse('newt-command-machine',
            args=(machine,)), {'command': '/bin/ls -a /'})
        self.assertEqual(r.status_code, 200)
        json_response = r.json()
        self.assertEqual(json_response['status'], "OK")
        # os.listdir() leaves off . and .. so add them in
        files = ['.', '..'] + os.listdir('/')
        files.sort()
        newtfiles = json_response['output']['output'].split()
        newtfiles.sort()
        self.assertEqual(files, newtfiles)
