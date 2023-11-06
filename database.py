import pymongo
from pymongo.mongo_client import MongoClient
import os

uri = os.environ.get('MongoDB_String')

cluster = MongoClient(uri)

db = cluster["school"]
collection = db["students"]

docs = [{"name": "John", "age": 30},{"name":"Chris", "age":25}, {"name":"Mary", "age":27}]

collection.insert_many(docs)