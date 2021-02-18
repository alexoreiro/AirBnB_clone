#!/usr/bin/python3
"""Test class City"""
from models.base_model import BaseModel
from models.city import City
import unittest


class Testcity(unittest.TestCase):
    """Tests for the City class"""

    def test_class_name(self):
        """Tests if class is named correctly"""

        city_example = City()
        self.assertEqual(city_example.__class__.__name__, "City")

    def test_inheritance(self):
        """Tests if Class inherits from BaseModel"""

        city_example = City()
        self.assertTrue(issubclass(city_example.__class__, BaseModel))
