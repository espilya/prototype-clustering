import pandas as pd

class DAO():
    def __init__(self, route):
        self.data = ""
        self.route = route
        self.extractData()

    
    def extractData(self):
        """
        Class for data extraction from csv, json, api,...
        Read and assign or updates self.data value 
        """
        pass

    def getData(self):
        return self.data

    def getPandasDataframe(self):
        return pd.read_json(self.data)
    

    