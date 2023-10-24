#!/usr/bin/python3
"""unittest for base"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class test_BaseModel(unittest.TestCase):
    """class for testing BaseModel"""

    def test_no_args_type(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id_pub(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_createat_public(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updatedat_public(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def unique_ids(self):
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.id, base2.id)

    def unique_created_at(self):
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.created_at, base2.created_at)


if __name__ == "__main__":
    unittest.main()
