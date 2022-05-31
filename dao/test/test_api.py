import unittest
import json

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from dao_csv import DAO_csv
from dao_json import DAO_json
from dao_linkedDataHub import DAO_linkedDataHub
from dao_api import DAO_api


class Test(unittest.TestCase):

    def test_api(self):
        # __user test__
        data_set = {
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
        json_dump = json.dumps(data_set)
        print(json_dump)
        _, response = DAO_api().updateUser(23, data_set)
        self.assertEqual(response.status_code, 200)

        # _, response = DAO_api().userCommunities("44")
        # self.assertEqual(response.status_code, 200)

        # #__community tests__
        # _, response = DAO_api().communityList()
        # self.assertEqual(response.status_code, 200)

        # _, response = DAO_api().communityDescription("621e53cf0aa6aa7517c2afdd")
        # self.assertEqual(response.status_code, 200)

        # _, response = DAO_api().communityUsers("621e53cf0aa6aa7517c2afdd")
        # self.assertEqual(response.status_code, 200)

    def test_linkedDataHub(self):
        _, response = DAO_linkedDataHub("https://api2.mksmart.org/object/89b71c31-4bd3-44ad-9573-420e6320e945").getData()
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()