#!/usr/bin/python3

""" Module tests/test_models/test_engine/test_file_storage"""

import models
from models.engine.file_storage import FileStorage
import os
from datetime import datetime
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import uuid
import unittest


class TestFile_Storage(unittest.TestCase):
    """ class TestFile_Storage """

    def test_docstring(self):
        """ function test_docstring """
        msj = "Module doesnt have docstring"
        obj = models.engine.file_storage.__doc__
        self.assertIsNotNone(obj, msj)
        msj = "Classes doesnt have docstring"
        self.assertIsNotNone(obj, msj)

    def test_executable_file(self):
        """ function test_executable_file """
        is_read_true = os.access("models/engine/file_storage.py", os.R_OK)
        self.assertTrue(is_read_true)
        is_write_true = os.access("models/engine/file_storage.py", os.W_OK)
        self.assertTrue(is_write_true)
        is_exec_true = os.access("models/engine/file_storage.py", os.X_OK)
        self.assertTrue(is_exec_true)

    def test_is_an_instance(self):
        """ function test_is_an_instance """
        my_model = FileStorage()
        self.assertIsInstance(my_model, FileStorage)

    def test_all(self):
        """tests if all method that returns dict __objects works properly"""
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._FileStorage__objects)

    def test_new(self):
        """test if new set key properly with user as example"""
        storage = FileStorage()
        obj = storage.all()
        user = User()
        user.id = "38f22813-2753-4d42-b37c-57a17f1e4f88"
        user.name = "Betty"
        storage.new(user)
        key = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(obj[key])
