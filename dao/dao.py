import os


class DAO():
    def __init__(self, route):
        """
        Construct of UGC objects.
            Parameters
            ----------
                route: str
                    Route to the csv, json, API url.  
            Notes
            -------
                You should process the information taken from csv, json, LinkedDataHub and store it as a json document. Store it in the variable "self.data".
                This is not the case for the API because the user generated content can be continuously updated at any moment. Thus, you need to perform mongoDB queries to retrieve the data instead.
                
                Don't try to fit the logic in this method if it takes more than 1-3 lines. Implement the methods (properly named) you need to handle the logic and retrieve it.
                In general, try to keep the classes and methods small and with clear functionality/responsibility.
        """
        self.route = route
        self.filename, self.file_extension = os.path.splitext(self.route)

    def getData(self):
        pass

    def readData(self):
        try:
            return self.data
        except AttributeError:
            self.getData()
            return self.data


    def jsonToPandasDataframe(self, json):
        """
        Method to get user generated content.

            Parameters
            ----------
                json: json document
            Returns
            -------
                Pandas Dataframe
        """   
        pass

    

    """
        The methods below deal with mongoDB queries in the case of the API.
    """
        
    def readUserGeneratedContents(self):
        """
        Method to get all user generated content.

            Parameters
            ----------

            Returns
            -------
            json document
        """
        pass
        
    def readUserGeneratedContent(self,id):
        """
        Method to get all user generated content.

            Parameters
            ----------
                id: str
                    user identifier

            Returns
            -------
            json document
        """
        pass
        
    def saveUserGeneratedContent(self, user):
        """
        Method to get user generated content.

            Parameters
            ----------
                user: json document
            Returns
            -------
                
        """   
        pass    
    
    def updateUserGeneratedContent(self, id, user):
        """
        Method to get user generated content.

            Parameters
            ----------
                id: str
                    user identifier
                user: json document
            Returns
            -------
               
        """   
        pass
        
    def deleteUserGeneratedContent(self, id):
        """
        Method to get user generated content.

            Parameters
            ----------
                id: str
                    user identifier
            Returns
            -------
              
        """   
        pass 