import pandas as pd
from dao import DAO

class DAO_csv(DAO):

    def __init__(self,route):
        super().__init__(route)
    
    def getData(self):
        self.data = pd.read_csv(self.route)
        
        
        

