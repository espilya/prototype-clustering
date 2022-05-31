import csv, json

from dao import DAO



class DAO_csv(DAO):

    def __init__(self, route):
        super().__init__(route)

    def extractData(self):
        self.data = []
        with open(self.route) as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                self.data.append(rows)
        self.data = json.dumps(self.data, sort_keys=True, indent=4)
    


        
        
        

