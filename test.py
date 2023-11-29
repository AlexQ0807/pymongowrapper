import os
import unittest
from pprint import pprint
from dotenv import load_dotenv

from pymongowrapper.dbwrapper import PyMongoDatabaseWrapper

load_dotenv()

MONGODB_USER = os.environ.get("MONGODB_USER")
MONGODB_PASS = os.environ.get("MONGODB_PASS")
MONGODB_HOST = os.environ.get("MONGODB_HOST")
MONGODB_DATABASE_NAME = os.environ.get("MONGODB_DATABASE_NAME")


class TestPyMongoDatabaseWrapper(unittest.TestCase):
    PMDW = PyMongoDatabaseWrapper(mongodb_user=MONGODB_USER,
                                  mongodb_pass=MONGODB_PASS,
                                  mongodb_host=MONGODB_HOST,
                                  mongodb_database_name=MONGODB_DATABASE_NAME)

    collection_name = 'pymongowrapper_test'

    def test_insert_one(self):
        try:
            obj = {'apple': 20, 'orange': 10, 'banana': 30}
            self.PMDW.collection_insert_one(collection_name=self.collection_name, insert_obj=obj)
            obj = {'apple': 10, 'orange': 20, 'banana': 30}
            self.PMDW.collection_insert_one(collection_name=self.collection_name, insert_obj=obj)

            results = self.PMDW.collection_filter(collection_name=self.collection_name, query_obj={'banana': 30})
            pprint(results, indent=2)
            self.assertTrue(True)
        except Exception as e:
            print(e)
            self.assertTrue(False)

    def test_update_one(self):
        try:
            self.PMDW.collection_update_one(collection_name=self.collection_name, query_obj={'apple': 20},
                                            update_obj={'orange': 100})
            results = self.PMDW.collection_filter(collection_name=self.collection_name, query_obj={'banana': 30})
            pprint(results, indent=2)
            self.assertTrue(True)
        except Exception as e:
            print(e)
            self.assertTrue(False)

    def test_delete_one(self):
        try:
            self.PMDW.collection_delete_one(collection_name=self.collection_name, query_obj={'orange': 100})

            results = self.PMDW.collection_filter(collection_name=self.collection_name, query_obj={'banana': 30})
            pprint(results, indent=2)
            self.assertTrue(True)
        except Exception as e:
            print(e)
            self.assertTrue(False)


    def test_delete_all(self):
        try:
            self.PMDW.collection_delete_all(collection_name=self.collection_name)

            results = self.PMDW.collection_filter(collection_name=self.collection_name, query_obj={})
            pprint(results, indent=2)
            self.assertTrue(True)
        except Exception as e:
            print(e)
            self.assertTrue(False)
