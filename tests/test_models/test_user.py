#!/usr/bin/python3

"""Test class User"""

from models.base_model import BaseModel
from models.user import User
from datetime import datetime
import uuid
import unittest


class Testuser(unittest.TestCase):
    """Tests for the User class"""

    def test_class_name(self):
        """Tests if class is named correctly"""
        user_example = User()
        self.assertEqual(user_example.__class__.__name__, "User")

    def test_inheritance(self):
        """Tests if class inherits from BaseModel"""
        user_example = User()
        self.assertTrue(issubclass(user_example.__class__, BaseModel))

    def test_user_id_format(self):
        """Tests if UUID is a string"""
        id_nbr = BaseModel()
        self.assertIsInstance(id_nbr.id, str)

    def test_user_created_at_format(self):
        """Tests if created_at is datetime format"""
        date = BaseModel()
        self.assertIsInstance(date.created_at, datetime)

    def test_user_updated_at_format(self):
        """Tests if date and time updated are in datetime format"""
        date = BaseModel()
        self.assertIsInstance(date.updated_at, datetime)
