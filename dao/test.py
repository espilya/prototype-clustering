from dao import DAO
import os
from dao_csv import DAO_csv
from dao_json import DAO_json
from dao_api import DAO_api
from dao_linkedDataHub import DAO_linkedDataHub



def main():
    
    route1 = r"data\IMMA\citizenInteractions.csv"
    route2 = r"data\MNCN\Sessions\sesion_jueves_11.json"
    route3 = r"a.api"
    route4 = r"a.linkedDataHub"

    route = route3

    filename, file_extension = os.path.splitext(route)
    if(file_extension == ".csv"):
        data = DAO_csv(route).readData()
    elif(file_extension == ".json"):
        data = DAO_json(route).readData()
    elif(file_extension == ".api"):
        pass #data = DAO_api(route).readData()
    elif(file_extension == ".linkedDataHub"):
        data = DAO_linkedDataHub(route).readData()
    else:
        data = "error"

    print(data)


main()