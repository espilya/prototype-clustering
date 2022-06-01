from bson.json_util import dumps, loads

from dao import DAO

import pymongo
from pymongo import MongoClient


class DAO_db_users(DAO):

    def __init__(self, route="mongodb://localhost:27017"):
        super().__init__(route)
        self.mongo = MongoClient(self.route)
        self.db_users = self.mongo.local.users

    def getData(self):
        raise ValueError('Incorrect operation. Please use a specific method for the API request')

    def getUsers(self):
        """devuelve un list de dict's"""
        data = self.db_users.find({}, {"_id": 0})
        return loads(dumps(list(data)))

    def getUser(self, userId):
        """devuelve un dict"""
        data = self.db_users.find({"id": userId}, {"_id": 0})
        data = loads(dumps(list(data)))
        if len(data) == 0:
            return {}
        return data[0]

    def replaceUser(self, userId, newJSON):
        response = self.db_users.replace_one({"id": userId}, loads(newJSON))
        return response

    def deleteUser(self, userId):
        response = self.db_users.delete_one({'id': userId})
        return response

    def insertUser(self, userJSON):
        """recibe un json string"""
        response = self.db_users.insert_one(loads(userJSON))
        return response

    def drop(self):
        self.db_users.drop()
