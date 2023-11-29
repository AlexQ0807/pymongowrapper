import certifi
from pymongo import MongoClient


class PyMongoDatabaseWrapper:
    ca = certifi.where()
    client_db = None

    def __init__(self, mongodb_user, mongodb_pass, mongodb_host, mongodb_database_name):
        try:
            uri = "mongodb+srv://{}:{}@{}/?retryWrites=true&w=majority".format(
                mongodb_user, mongodb_pass, mongodb_host
            )

            # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
            client = MongoClient(uri, tlsCAFile=self.ca)

            self.client_db = client[mongodb_database_name]
        except Exception as e:
            raise e

    def collection_filter(self, collection_name: str, query_obj: dict, result_fields_obj=None):
        '''
        NOTE: result_fields_obj example:
        {"id": 1, "update_date": 1 } => will show only the id and update_date fields per result

        :param collection_name:
        :param query_obj:
        :param result_fields_obj:
        :return:
        '''
        try:
            if result_fields_obj is None:
                result_fields_obj = {}

            query_results = self.client_db[collection_name].find(query_obj, result_fields_obj)
            return [item for item in query_results]
        except Exception as e:
            raise e

    def collection_find_all(self, collection_name: str, result_fields_obj=None):
        try:
            if result_fields_obj is None:
                result_fields_obj = {}

            query_results = self.client_db[collection_name].find({}, result_fields_obj)
            return [item for item in query_results]
        except Exception as e:
            raise e

    def collection_insert_one(self, collection_name, insert_obj):
        try:
            self.client_db[collection_name].insert_one(insert_obj)
            print("INSERTED new item to collection name {}: {}".format(collection_name, insert_obj))
        except Exception as e:
            raise e

    def collection_update_one(self, collection_name, query_obj, update_obj):
        try:
            set_values_obj = {"$set": update_obj}

            collection = self.client_db[collection_name]
            collection.update_one(query_obj, set_values_obj)
            print("UPDATED item in collection name {}: {}".format(collection_name, query_obj))
        except Exception as e:
            raise e

    def collection_delete_one(self, collection_name, query_obj):
        try:
            self.client_db[collection_name].delete_one(query_obj)
            print("DELETED item from collection name {}: {}".format(collection_name, query_obj))
        except Exception as e:
            raise e

    def collection_delete_all(self, collection_name):
        try:
            self.collection_delete_one(collection_name, {})
            print("DELETED all items from collection name {}".format(collection_name))
        except Exception as e:
            raise e