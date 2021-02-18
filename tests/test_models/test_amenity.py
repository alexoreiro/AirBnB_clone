#!/usr/bin/python3
"""Test class Amenity"""
from models.base_model import BaseModel
from models.amenity import Amenity
import unittest


class Testamenity(unittest.TestCase):
    """Test for amenity class"""

    def test_class_name(self):
        """ Tests if the class is named correctly"""

        amenity_example = Amenity()
        self.assertEqual(amenity_example.__class__.__name__, "Amenity")

    def test_inheritance(self):
        """Tests if the class inherits from BaseModel"""

        amenity_example = Amenity()
        self.assertTrue(issubclass(amenity_example.__class__, BaseModel))
