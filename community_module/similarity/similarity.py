# Authors: Guillermo Jimenez-Díaz
#          Jose Luis Jorro-Aragoneses

class Similarity:
    """Class to define the functions to be implemented to calculate
    the similarity between elements.
    """

    def distance(elemA, elemB):
        """Method to obtain the distance between two element.

        Parameters
        ----------
        elemA : int
            Id of first element. This id should be in self.data.
        elemB : int
            Id of second element. This id should be in self.data.

        Returns
        -------
        double
            Distance between the two elements.
        """
        pass

    def similarity(elemA, elemB):
        """Method to obtain the similarity between two element.

        Parameters
        ----------
        elemA : int
            Id of first element. This id should be in self.data.
        elemB : int
            Id of second element. This id should be in self.data.

        Returns
        -------
        double
            Distance between the two elements.
        """
        pass

    def matrix_distance(self):
        """Method to calculate the matrix of distance between all element included in data.

        Returns
        -------
        np.array
            Matrix that contains all similarity values.
        """
        pass

    def matrix_similarity(self):
        """Method to calculate the matrix of similarity between all element included in data.

        Returns
        -------
        np.array
            Matrix that contains all similarity values.
        """
        pass