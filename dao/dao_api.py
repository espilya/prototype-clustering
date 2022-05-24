import json
from dao import DAO

import requests
from requests.auth import HTTPBasicAuth

class DAO_api(DAO):

    def __init__(self,route):
        super().__init__(route)
    
    def getData(self):
        uuid = "xxx-xxx-xxx"
        response = requests.get("http://spice.fdi.ucm.es/v1.1/communities")
        print("status_code", response.status_code)
        self.data = response.json()
        self.data = json.dumps(self.data, sort_keys=True, indent=4)


    def readData(self):
        try:
            return self.data
        except AttributeError:
            self.getData()
            return self.data
    
    """
        The methods below deal with mongoDB queries in the case of the API.
    """
    def readUserGeneratedContents(self):
        """
        Method to get all user generated content.
            Parameters
            ----------
            Returns
            -------
            json document
        """
        response = requests.get("http://spice.fdi.ucm.es/v1.1/communities")
        print("status_code", response.status_code)
        self.data = response.json()
        self.data = json.dumps(self.data, sort_keys=True, indent=4)
        return self.data
        
    def readUserGeneratedContent(self, id):
        response = requests.get("http://spice.fdi.ucm.es/v1.1/users/{}/communities".format(id))
        print("status_code", response.status_code)
        self.dataUGC = response.json()
        self.dataUGC = json.dumps(self.dataUGC, sort_keys=True, indent=4)
        return self.dataUGC
        
    def saveUserGeneratedContent(self, user):
        response = requests.post("", data=user)
        print("status_code", response.status_code)
      
    
    def updateUserGeneratedContent(self, id, user): 
        response = requests.post("http://spice.fdi.ucm.es/v1.1/users/{}/update-generated-content".format(id), data=user)
        print("status_code", response.status_code)
  
        
    def deleteUserGeneratedContent(self, id):  
        response = requests.post()
        print("status_code", response.status_code)


