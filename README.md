## Wrapper for PyMongo (Private)
<hr>

### Setup
```
pip install git+https://github.com/AlexQ0807/pymongowrapper.git
```


### Example

```
from dotenv import load_dotenv
from pymongowrapper.dbwrapper import PyMongoDatabaseWrapper

load_dotenv()

MONGODB_USER = os.environ.get("MONGODB_USER")
MONGODB_PASS = os.environ.get("MONGODB_PASS")
MONGODB_HOST = os.environ.get("MONGODB_HOST")
MONGODB_DATABASE_NAME = os.environ.get("MONGODB_DATABASE_NAME")

PMDW = PyMongoDatabaseWrapper(mongodb_user=MONGODB_USER,
                              mongodb_pass=MONGODB_PASS,
                              mongodb_host=MONGODB_HOST,
                              mongodb_database_name=MONGODB_DATABASE_NAME)

obj = {'apple': 20, 'orange': 10, 'banana': 30}
self.PMDW.collection_insert_one(collection_name=self.collection_name, insert_obj=obj)
obj = {'apple': 10, 'orange': 20, 'banana': 30}
self.PMDW.collection_insert_one(collection_name=self.collection_name, insert_obj=obj)

results = self.PMDW.collection_filter(collection_name=self.collection_name, query_obj={'banana': 30})
pprint(results, indent=2)

```