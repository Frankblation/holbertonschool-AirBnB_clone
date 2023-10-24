#!/usr/bin/python3
"""unittests for models/amenity.py."""
import unittest
from datetime import datetime
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """unittests for amenity class"""

    def test_no_arg(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_updated_at_pub(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_created_at_pub(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_to_dict(self):
        am = Amenity()
        self.assertIn("id", am.to_dict())
        self.assertIn("created_at", am.to_dict())
        self.assertIn("updated_at", am.to_dict())
        self.assertIn("__class__", am.to_dict())
