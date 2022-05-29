import json
from bson.json_util import dumps

from dao import DAO

import pymongo
from pymongo import MongoClient


class DAO_db(DAO):

    def __init__(self,route):
        super().__init__(route)
        self.mongo = MongoClient("mongodb://localhost:27017")
        self.db_users = self.mongo.local.users
        
    def getData(self):
        raise ValueError('Incorrect operation. Please use a specific method for the API request')

    def readAll(self):
        data = self.db_users.find()
        return dumps(list(data))

    def read(self, id):
        data = self.db_users.find({"id": id})
        return dumps(list(data))

    def update(self, user, newvalues):
        response = self.db_users.update_one({"id": user}, newvalues)
        return response
         
    def add(self, user):
        response = self.db_users.insert_one(user)
        return response

    def close(self):
        self.mongo.close()


