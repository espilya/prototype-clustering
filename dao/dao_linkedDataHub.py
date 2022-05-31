import json
from dao import DAO

import requests
from requests.auth import HTTPBasicAuth

class DAO_linkedDataHub(DAO):

    def __init__(self, route):
        super().__init__(route)

    def getData(self):
        return self.data, self.response
    
    def extractData(self):
        uuid = "xxx"
        self.response = requests.get(self.route, auth = HTTPBasicAuth(uuid, uuid))
        self.data = self.response.json()




            
        

        