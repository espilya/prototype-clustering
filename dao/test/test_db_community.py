import unittest
import json

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from dao_db_community import DAO_db_community




class Test_community(unittest.TestCase):

    def test_db_community(self):
        pass


if __name__ == '__main__':
    unittest.main()