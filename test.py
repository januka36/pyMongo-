import pymongo
from pymongo.mongo_client import MongoClient
import os

uri = os.environ.get('MongoDB_String')
print(type(uri))

cluster = MongoClient("mongodb+srv://janukasf:3366@cluster0.h2brxcb.mongodb.net/?retryWrites=true&w=majority")
print("Authhhhhhhhhhhh")

try:
    cluster.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)