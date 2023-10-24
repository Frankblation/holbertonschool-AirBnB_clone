#!/usr/bin/python3
"""unittests for review.py."""
import unittest
from datetime import datetime
from models.review import Review


class TestReview(unittest.TestCase):
    """unittests for Review class"""

    def test_no_arg(self):
        self.assertEqual(Review, type(Review()))

    def test_updated_at_pub(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_created_at_pub(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_to_dict(self):
        rev = Review()
        self.assertIn("id", rev.to_dict())
        self.assertIn("created_at", rev.to_dict())
        self.assertIn("updated_at", rev.to_dict())
        self.assertIn("__class__", rev.to_dict())
