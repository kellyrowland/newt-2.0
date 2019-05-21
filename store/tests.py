from django.test import TestCase
from django.conf import settings
from django.urls import reverse
import json
from newt.tests import MyTestClient, newt_base_url, login
from authnz import urls

class StoreTests(TestCase):
    fixtures = ["test_fixture.json"]

    def setUp(self):
        self.client = MyTestClient()
        # Hacky: Need to figure out a way around this...
        try:
            from pymongo import MongoClient
            db = MongoClient()['store']
            db.test_store_1.drop()
            db.permissions.remove({"name":"test_store_1"})
        except Exception:
            pass
        try:
            import redis
            storedb = redis.Redis(host="localhost", db=0)
            storedb.flushdb()
        except Exception:
            pass

    def test_store_basic(self):
        self.client.post(reverse('newt-auth'), data=login)

        r = self.client.post(reverse('newt-store'))
        self.assertEqual(r.status_code, 200)

    def test_store_manipulation(self):
        self.client.post(reverse('newt-auth'), data=login)

        # Creates a new store (create_store)
        r = self.client.post(reverse('newt-store'))
        self.assertEqual(r.status_code, 200)
        json_response = r.json()

        # Ensures that no data was added to the store
        self.assertEqual(json_response['output']['oid'], [])
        store_id = json_response['output']['id']
        
        # Ensures that new store is empty (get_store_contents)
        r = self.client.get(reverse('newt-store-name',args=(store_id,)))
        self.assertEqual(r.status_code, 200)
        json_response = r.json()
        self.assertEqual(json_response['output'], [])
        
        # Tests insertion (store_insert)
        payload = {"data": {"foo":"bar"}}
        r = self.client.post(reverse('newt-store-name',kwargs={'store_name': store_id}), {"foo":"bar"})
        self.assertEqual(r.status_code, 200)
        json_response = r.json()
        obj_id = json_response['output']

        # Checks insertion by checking all of the store's objects (get_store_contents)
        r = self.client.get(reverse('newt-store-name',args=(store_id,)))
        self.assertEqual(r.status_code, 200)
        json_response = r.json()
        self.assertEqual(json_response['output'][0]['data'], payload['data'])
        self.assertEqual(json_response['output'][0]['oid'], obj_id)

        # Checks insertion by checking the individual object (store_get_obj)
        r = self.client.get(reverse('newt-store-name-id',args=(store_id,obj_id,)))
        self.assertEqual(r.status_code, 200)
        json_response = r.json()
        self.assertEqual(json_response['output'], payload['data'])
        
        # Tests update (store_update)
        updated_payload = {"data": {"foo": "baz"}}
        r = self.client.put(reverse('newt-store-name-id',
            kwargs={'store_name':store_id,'obj_id':obj_id}), {"foo": "baz"})
        self.assertEqual(r.status_code, 200)
        json_response = r.json()
        self.assertEqual(json_response['output'], obj_id)

        # Checks updated data
        r = self.client.get(reverse('newt-store-name-id',args=(store_id,obj_id,)))
        self.assertEqual(r.status_code, 200)
        json_response = r.json()
        self.assertEqual(json_response['output'], updated_payload['data'])

        # Tests delete
        r = self.client.delete(reverse('newt-store-name',args=(store_id,)))
        self.assertEqual(r.status_code, 200)
        json_response = r.json()
        self.assertEqual(json_response['output'], store_id)

        # Ensures that getting the deleted store will error
        r = self.client.get(reverse('newt-store-name',args=(store_id,)))
        self.assertEqual(r.status_code, 404)        

    def test_store_creation_with_initial(self):
        self.client.post(reverse('newt-auth'), data=login)

        payload = {"data": {"x":5}}

        # Without an initial name
        r = self.client.post(reverse('newt-store'), {"x":5})
        self.assertEqual(r.status_code, 200)
        json_response = r.json()
        store_id = json_response['output']['id']
        self.assertEqual(len(json_response['output']['oid']), 1)
        obj_id = json_response['output']['oid'][0]

        # Checks the data
        r = self.client.get(reverse('newt-store-name-id'))
        self.assertEqual(r.status_code, 200)
        json_response = r.json()
        self.assertEqual(json_response['output'], payload['data'])

        # With an initial name
        r = self.client.post(reverse('newt-store-name',kwargs={'store_name': "teststore1"}), {"x":5})
        self.assertEqual(r.status_code, 200)
        json_response = r.json()
        self.assertEqual(json_response['output']['id'], "teststore1")
        self.assertEqual(len(json_response['output']['oid']), 1)
        obj_id = json_response['output']['oid'][0]

        # Checks the data
        r = self.client.get(reverse('newt-store-name-id'))
        self.assertEqual(r.status_code, 200)
        json_response = r.json()
        self.assertEqual(json_response['output'], payload['data'])

        # Deletes the store
        r = self.client.delete(reverse('newt-store-name'))
        self.assertEqual(r.status_code, 200)
        json_response = r.json()
        self.assertEqual(json_response['output'], "teststore1")
        r = self.client.delete(reverse('newt-store-name-id'))
        self.assertEqual(r.status_code, 200)
        json_response = r.json()
        self.assertEqual(json_response['output'], store_id)

    def test_store_perms(self):
        self.client.post(reverse('newt-auth'), data=login)

        # Create a store
        r = self.client.post(reverse('newt-store-name',args=("test_store_1",)))
        self.assertEqual(r.status_code, 200)
        r = self.client.get(reverse('newt-store-perms',args=("test_store_1",)))
        self.assertEqual(r.status_code, 200)
        json_response = r.json()
        # Checks that the creator has appropriate permissions
        self.assertEqual(json_response['output']['name'], "test_store_1")
        self.assertEqual(json_response['output']['perms'][0]['name'], login['username'])
        self.assertIn("r", json_response['output']['perms'][0]['perms'])
        self.assertIn("w", json_response['output']['perms'][0]['perms'])

        payload = {"data": json.dumps([{"name": login['username'], "perms": ["r", "w", "x"]}])}
        r = self.client.post(reverse("newt-store-perms", kwargs={"store_name":"test_store_1"}), payload)
        self.assertEqual(r.status_code, 200)

        r = self.client.get(reverse('newt-store-perms',args=("test_store_1",)))
        self.assertEqual(r.status_code, 200)
        json_response = r.json()
        self.assertEqual(json_response['output']['name'], "test_store_1")
        self.assertEqual(json_response['output']['perms'][0]['name'], login['username'])
        self.assertIn("r", json_response['output']['perms'][0]['perms'])
        self.assertIn("w", json_response['output']['perms'][0]['perms'])
        self.assertIn("x", json_response['output']['perms'][0]['perms'])

        # Deletes the store
        r = self.client.delete(reverse('newt-store-name',args=("test_store_1",)))
        self.assertEqual(r.status_code, 200)
        r = self.client.get(reverse('newt-store-perms',args=("test_store_1",)))
        self.assertEqual(r.status_code, 404)
