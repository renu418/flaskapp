from pymongo import *


class MongoHandler:
    def __init__(self):
        try:
            self.client = MongoClient()
            print("________________DATABASE CONNECTED____________________")
        except:
            print("________________DATABASE NOT CONNECTED____________________")

    def insert(self, db, collection, data):
        self.db = self.client[db]
        self.collection = self.db[collection]
        self.collection.insert_one(data)
