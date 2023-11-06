import pymongo
from pymongo.mongo_client import MongoClient
import os

uri = os.environ.get('MongoDB_String')

cluster = MongoClient(uri)
print("Authhhhhhhhhhhh")

try:
    cluster.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)