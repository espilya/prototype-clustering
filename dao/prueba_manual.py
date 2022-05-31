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

    dao = DAO_db_users()
    data = {"id": "001"}
    d= dao.add(data)
    print(d)
    print(dir(d))
    print(d.acknowledged)
    d = dao.readUser("004")
    print(d)
    data = {"id": "002"}
    dao.add(data)
    # print(dao.readAll())
    # print(dao.read("001"))

    newvalues = { "$set": { 'id': "009" } }
    # print(dao.update("001", newvalues))
    # print(dao.read("009"))

    dao.close()

    # userId = 23
    # data = {
    #             "id": 23,
    #             "userid": 23,
    #             "origin": "90e6d701748f08514b01",
    #             "source_id": "90e6d701748f08514b01",
    #             "source": "Content description",
    #             "pname": "DemographicGender",
    #             "pvalue": "F (for Female value)",
    #             "context": "application P:DemographicsPrep",
    #             "datapoints": 0
    #         }
    # # data = json.dumps(data, ensure_ascii=True, sort_keys=True)
    # response = requests.post("http://spice.fdi.ucm.es/v1.1/users/23/update-generated-content", json=data)
    # print(response.status_code)
    
    return
    route1 = r"data\IMMA\citizenInteractions.csv"
    route2 = r"data\IMMA\artworks_IMMA.json"
    route3 = r"a.api"
    route4 = r"a.linkedDataHub"
    route5 = r"db"

    route = route1
    
    dao = DAO_db(route)
    data_set = {
                        "id": "23",
                        "userid": "23",
                        "origin": "90e6d701748f08514b01",
                        "source_id": "90e6d701748f08514b01",
                        "source": "Content description",
                        "pname": "DemographicGender",
                        "pvalue": "F (for Female value)",
                        "context": "application P:DemographicsPrep",
                        "datapoints": 0
                    }
    json_dump = json.dumps(data_set)
    dao.add(data_set)
    data = {"id": "002"}
    dao.add(data)
    print(dao.readAll())
    print(dao.read("001"))

    newvalues = { "$set": { 'id': "009" } }
    print(dao.update("001", newvalues))
    print(dao.read("009"))

    dao.close()
    


    # filename, file_extension = os.path.splitext(route)
    # if(file_extension == ".csv"):
    #     data = DAO_csv(route).getData()
    # elif(file_extension == ".json"):
    #     data = DAO_json(route).getData()
    # elif(file_extension == ".api"):
    #     #data = DAO_api(route).getData()
    #     data = DAO_api(route).communityDescription("621e53cf0aa6aa7517c2afdd")
    # elif(file_extension == ".linkedDataHub"):
    #     data = DAO_linkedDataHub("https://api2.mksmart.org/object/89b71c31-4bd3-44ad-9573-420e6320e945").getData()
    # else:
    #     data = "error"

    # print(data)


main()