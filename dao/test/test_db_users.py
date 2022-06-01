import unittest
import json
import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from dao_db_users import DAO_db_users

from bson.json_util import dumps, loads


class Test_db_users(unittest.TestCase):

    def setUp(self):
        self.dao = DAO_db_users()

    def tearDown(self):
        self.dao.drop()

    """
    an'ade un usuario en la db, lo elimina y lo intenta leer
    """

    def test_deleteUser(self):
        user = {"id": "001"}
        self.dao.insertUser(json.dumps(user))
        self.dao.deleteUser("001")
        response = self.dao.getUser("001")
        self.assertEqual(response, {})

    """
    an'ade un usuario en la db y despues lo lee. 
    despues compara el usuario que creo y el que recibio de la db
    """

    def test_add_and_getUser(self):
        user = {
            "id": "001",
            "gender": "F",
            "cars": ["Ford", "BMW", "Fiat"]
        }
        self.dao.insertUser(json.dumps(user))
        response = self.dao.getUser("001")
        self.assertEqual(response, user)
        self.dao.deleteUser("001")

    """an'ade 2 usuarios, los lee y despues compara"""

    def test_add_and_getUsers(self):
        user1 = {"id": "001"}
        user2 = {"id": "002"}
        self.dao.insertUser(json.dumps(user1))
        self.dao.insertUser(json.dumps(user2))
        response = self.dao.getUsers()
        self.assertIn(user1, response)
        self.assertIn(user2, response)
        self.dao.deleteUser("001")
        self.dao.deleteUser("002")

    """
    an'ade un usuario en la db, le cambia el id a '009' y despues lo lee.
    al final compara el id del usuario recibido con el '009'
    """

    def test_replace(self):
        user = {"id": "001"}
        newUserValues = {"id": "009"}
        self.dao.insertUser(json.dumps(user))
        self.dao.replaceUser("001", json.dumps(newUserValues))
        response = self.dao.getUser("009")
        self.assertEqual(response.get("id"), "009")
        self.dao.deleteUser("009")

    def test_valueError(self):
        with self.assertRaises(ValueError):
            self.dao.getData()


if __name__ == '__main__':
    unittest.main()
