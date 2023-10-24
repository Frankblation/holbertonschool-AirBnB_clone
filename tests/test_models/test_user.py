#!/usr/bin/python3
"""unittests for models/user.py."""
import unittest
from datetime import datetime
from models.user import User


class TestAmenity(unittest.TestCase):
    """unittests for User class"""

    def test_no_arg(self):
        self.assertEqual(User, type(User()))

    def test_updated_at_pub(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_created_at_pub(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_to_dict(self):
        us = User()
        self.assertIn("id", us.to_dict())
        self.assertIn("created_at", us.to_dict())
        self.assertIn("updated_at", us.to_dict())
        self.assertIn("__class__", us.to_dict())
