from dao import DAO
import os
from dao_csv import DAO_csv
from dao_json import DAO_json
from dao_api import DAO_api
from dao_linkedDataHub import DAO_linkedDataHub



def main():
    
    route1 = r"data\IMMA\citizenInteractions.csv"
    route2 = r"data\IMMA\artworks_IMMA.json"
    route3 = r"a.api"
    route4 = r"a.linkedDataHub"

    route = route3

    filename, file_extension = os.path.splitext(route)
    if(file_extension == ".csv"):
        data = DAO_csv(route).getData()
    elif(file_extension == ".json"):
        data = DAO_json(route).getData()
    elif(file_extension == ".api"):
        #data = DAO_api(route).getData()
        data = DAO_api(route).communityList()
    elif(file_extension == ".linkedDataHub"):
        data = DAO_linkedDataHub("https://api2.mksmart.org/object/89b71c31-4bd3-44ad-9573-420e6320e945").getData()
    else:
        data = "error"

    print(data)


main()