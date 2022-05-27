import pandas as pd
from dao import DAO
import os



class DAO_csv(DAO):

    def __init__(self, route):
        super().__init__(route)

    def extractData(self):
        self.data = pd.read_csv(self.route)
        
        
        

