#!/usr/bin/python3
"""Test class Review"""
from models.base_model import BaseModel
from models.review import Review
import unittest


class Testreview(unittest.TestCase):
    """tests for the Review class"""

    def test_class_name(self):
        """Tests if class is named correctly"""

        review_example = Review()
        self.assertEqual(review_example.__class__.__name__, "Review")

    def test_inheritance(self):
        """Tests if Class inherits from BaseModel"""

        review_example = Review()
        self.assertTrue(issubclass(review_example.__class__, BaseModel))
