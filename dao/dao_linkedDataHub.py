import json
from dao import DAO

import requests
from requests.auth import HTTPBasicAuth

class DAO_linkedDataHub(DAO):

    def __init__(self, route):
        super().__init__(route)
    
    def extractData(self):
        uuid = "xxx-xxx-xxx"
        response = requests.get(self.route, auth = HTTPBasicAuth(uuid, uuid))
        print("status_code", response.status_code)
        self.data = response.json()




            
        

        