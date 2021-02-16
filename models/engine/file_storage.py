#!/usr/bin/python3
"""
FileStorage seralizes instances to JSON file and deseralizes fils to instances
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review


class FileStorage():
    """
    serializes instances to a JSON file and deserializes JSON file to instances
    __file_path: path to JSON file
    __objects: empty dictionary that will store all objects
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return (self.__objects)

    def new(self, obj):
        """
        sets in __objects the obj key
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        serializes __objects to JSON file path
        """
        cereal = {}
        for key, value in self.__objects.items():
            cereal[key] = value.to_dict()
        with open(self.__file_path, mode='w') as c_file:
            json.dump(cereal, c_file)

    def reload(self):
        """
        desearializes the JSON file to __objects
        """
        new_dict = {}
        try:
            with open(self.__file_path, mode='r') as r_file:
                new_dict = json.load(r_file)
                for key, value in new_dict.items():
                    new_obj = eval(value["__class__"])(**value)
                    self.__objects[key] = new_obj
        except FileNotFoundError:
            pass
