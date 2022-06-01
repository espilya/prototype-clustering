import unittest
import json

import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from dao_db_community import DAO_db_community


class Test_community(unittest.TestCase):

    def setUp(self):
        self.dao = DAO_db_community()

    def tearDown(self):
        self.dao.drop()

    """
    an'ade un usuario en la db, lo elimina y lo intenta leer
    """

    def test_deleteCommunity(self):
        data = {"id": "001"}
        self.dao.insertCommunity(json.dumps(data))
        self.dao.deleteCommunity("001")
        response = self.dao.getCommunity("001")
        self.assertEqual(response, {})

    """
    an'ade un usuario en la db y despues lo lee. 
    despues compara el usuario que creo y el que recibio de la db
    """

    def test_add_and_getCommunity(self):
        data = {
            "id": "001",
            "explanation": "asdasdasda ggaf vasfopaor",
            "users": ["001", "002", "003"]
        }
        self.dao.insertCommunity(json.dumps(data))
        response = self.dao.getCommunity("001")
        self.assertEqual(response, data)
        self.dao.deleteCommunity("001")

    """an'ade 2 usuarios, los lee y despues compara"""

    def test_add_and_getCommunities(self):
        data1 = {"id": "001"}
        data2 = {"id": "002"}
        self.dao.insertCommunity(json.dumps(data1))
        self.dao.insertCommunity(json.dumps(data2))
        response = self.dao.getCommunities()
        self.assertIn(data1, response)
        self.assertIn(data2, response)
        self.dao.deleteCommunity("001")
        self.dao.deleteCommunity("002")

    """
    an'ade un usuario en la db, le cambia el id a '009' y despues lo lee.
    al final compara el id del usuario recibido con el '009'
    """

    def test_replace(self):
        data = {"id": "001"}
        newCommunityValues = {"id": "009"}
        self.dao.insertCommunity(json.dumps(data))
        self.dao.replaceCommunity("001", json.dumps(newCommunityValues))
        response = self.dao.getCommunity("009")
        self.assertEqual(response.get("id"), "009")
        self.dao.deleteCommunity("009")

    def test_updates(self):
        data = {
            "id": "001",
            "explanation": "asdasdasda ggaf vasfopaor"
        }
        newCommunityExplanation = "Older than 70"
        self.dao.insertCommunity(json.dumps(data))
        self.dao.updateExplanation("001", "Older than 70")
        response = self.dao.getCommunity("001")
        self.assertEqual(response.get("explanation"), newCommunityExplanation)
        self.dao.deleteCommunity("001")

    def test_addUser(self):
        data = {
            "id": "123",
            "explanation": "asdasdasda ggaf vasfopaor",
            "users": ["001", "002", "003"]
        }
        newUser = "009"
        self.dao.insertCommunity(json.dumps(data))
        self.dao.addUserToCommunity("123", newUser)
        response = self.dao.getCommunityUsers("123")
        self.assertIn(newUser, response.get("users"))
        self.dao.deleteCommunity("123")

    def test_valueError(self):
        with self.assertRaises(ValueError):
            self.dao.getData()


if __name__ == '__main__':
    unittest.main()
