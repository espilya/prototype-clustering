

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
    
    def jsonToPandasDataframe(self, json):
        """
            Parameters
            ----------
                json: json document
            Returns
            -------
                Pandas Dataframe
        """   
        pass

    