#!/usr/bin/python3
"""Test class State"""
from models.base_model import BaseModel
from models.state import State
import unittest


class Teststate(unittest.TestCase):
    """Tests for the Place class"""

    def test_class_name(self):
        """Tests if class is named correctly"""

        state_example = State()
        self.assertEqual(state_example.__class__.__name__, "State")

    def test_inheritance(self):
        """Tests if Class inherits from BaseModel"""

        state_example = State()
        self.assertTrue(issubclass(state_example.__class__, BaseModel))
