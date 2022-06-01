import json
from bson.json_util import dumps, loads

from dao import DAO

import pymongo
from pymongo import MongoClient


class DAO_db_community(DAO):

    def __init__(self, route="mongodb://localhost:27017"):
        super().__init__(route)
        self.mongo = MongoClient(self.route)
        self.db_communities = self.mongo.local.communities

    def getData(self):
        raise ValueError('Incorrect operation. Please use a specific method for the API request')

    def deleteCommunity(self, communityId):
        response = self.db_communities.delete_one({'id': communityId})
        return response

    def insertCommunity(self, communityJSON):
        response = self.db_communities.insert_one(loads(communityJSON))
        return response

    def getCommunities(self):
        data = self.db_communities.find({}, {"_id": 0})
        return loads(dumps(list(data)))

    def getCommunity(self, communityId):
        data = self.db_communities.find({"id": communityId}, {"_id": 0})
        data = loads(dumps(list(data)))
        if len(data) == 0:
            return {}
        return data[0]

    def getCommunityUsers(self, communityId):
        data = self.db_communities.find({"id": communityId}, {"users": 1, "_id": 0})
        return loads(dumps(list(data)))[0]

    def addUserToCommunity(self, communityId, newUserId):
        response = self.db_communities.update_one(
            {"id": communityId},
            {
                "$push": {
                    "users": newUserId
                }
            }
        );
        return response

    def replaceCommunity(self, communityId, newJSON):
        response = self.db_communities.replace_one({"id": communityId}, loads(newJSON))
        return response

    def updateExplanation(self, communityId, newValue):
        response = self.db_communities.update_one(
            {"id": communityId},
            {
                "$set": {
                    "explanation": newValue
                }
            }
        )
        return response

    def drop(self):
        self.db_communities.drop()
