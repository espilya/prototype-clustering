import unittest
import json

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from dao_csv import DAO_csv
from dao_json import DAO_json



def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True

class Test_file(unittest.TestCase):

    def test_json(self):
        route = r"data\MNCN\Sessions\sesion_jueves_11.json"
        data = DAO_json(route).getData()
        self.assertTrue(validateJSON(data))

    def test_csv(self):
        route = r"data\IMMA\citizenInteractions.csv"
        data = DAO_csv(route).getData()
        self.assertTrue(validateJSON(data))

if __name__ == '__main__':
    unittest.main()