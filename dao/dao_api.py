import json
from dao import DAO

import requests
from requests.auth import HTTPBasicAuth

class DAO_api(DAO):

    def __init__(self,route):
        super().__init__(route)
    
    def getData(self):
        uuid = "xxx-xxx-xxx"
        response = requests.get("https://api2.mksmart.org/object/89b71c31-4bd3-44ad-9573-420e6320e945", auth = HTTPBasicAuth(uuid, uuid))
        print("status_code", response.status_code)
        self.data = response.json()


    def readData(self):
        try:
            return json.dumps(self.data, sort_keys=True, indent=4)
        except AttributeError:
            self.getData()
            return json.dumps(self.data, sort_keys=True, indent=4)
    
