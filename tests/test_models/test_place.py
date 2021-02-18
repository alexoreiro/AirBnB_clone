#!/usr/bin/python3
"""Test class Place"""
from models.base_model import BaseModel
from models.place import Place
import unittest


class Testplace(unittest.TestCase):
    """tests for the Place class"""

    def test_class_name(self):
        """Tests if class is named correctly"""

        place_example = Place()
        self.assertEqual(place_example.__class__.__name__, "Place")

    def test_inheritance(self):
        """Tests if Class inherits from BaseModel"""

        place_example = Place()
        self.assertTrue(issubclass(place_example.__class__, BaseModel))
