import pymongo
from pymongo.mongo_client import MongoClient
import os

uri = os.environ.get('MongoDB_String')

cluster = MongoClient(uri)

db = cluster["school"]
collection = db["students"]

def alter_docs(name, age):
    doc = collection.find_one({"name" : name})
    collection.update_one({"name":name},{"$set":{"age":age}})

def read_docs():
    docs = collection.find()
    for doc in docs:
        print (doc["name"], doc["age"])

alter_docs("John", 28)
read_docs()





