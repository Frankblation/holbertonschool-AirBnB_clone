#!/usr/bin/python3
"""unittests for place.py."""
import unittest
from datetime import datetime
from models.place import Place


class TestPlace(unittest.TestCase):
    """unittests for place class"""

    def test_no_arg(self):
        self.assertEqual(Place, type(Place()))

    def test_updated_at_pub(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_created_at_pub(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_to_dict(self):
        pl = Place()
        self.assertIn("id", pl.to_dict())
        self.assertIn("created_at", pl.to_dict())
        self.assertIn("updated_at", pl.to_dict())
        self.assertIn("__class__", pl.to_dict())
