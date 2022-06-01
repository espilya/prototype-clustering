import re
from dao import DAO
import os
from dao_db_users import DAO_db_users

from dao_csv import DAO_csv
from dao_json import DAO_json
from dao_api import DAO_api
from dao_linkedDataHub import DAO_linkedDataHub
import json

import requests
from requests.auth import HTTPBasicAuth

def main():

    userId = 23
    data = {
                "id": 23,
                "userid": 23,
                "origin": "90e6d701748f08514b01",
                "source_id": "90e6d701748f08514b01",
                "source": "Content description",
                "pname": "DemographicGender",
                "pvalue": "F (for Female value)",
                "context": "application P:DemographicsPrep",
                "datapoints": 0
            }
    # data = json.dumps(data, ensure_ascii=True, sort_keys=True)
    response = requests.post("http://spice.fdi.ucm.es/v1.1/users/23/update-generated-content", json=data)
    print(response.status_code)
    
    return


main()