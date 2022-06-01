import json

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from dao import DAO


class DAO_json(DAO):

    def __init__(self,route):
        super().__init__(route)

    
    def extractData(self):
        with open(self.route, 'r', encoding='utf8') as f:
            self.data = json.load(f)
            self.data = json.dumps(self.data, sort_keys=True, indent=4)
