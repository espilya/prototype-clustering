import json
from dao import DAO

class DAO_json(DAO):

    def __init__(self,route):
        super().__init__(route)
    
    def getData(self):
        with open(self.route, 'r', encoding='utf8') as f:
            self.data = json.load(f)
