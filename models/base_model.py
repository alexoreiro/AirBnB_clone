#!/usr/bin/python3
"""
BaseModel class that will be used by all instances
"""


import models
from datetime import datetime
import uuid
import json


class BaseModel():
    """
    BaseModel class that defines all common attributes/methods
    for other classes
    """
    def __init__(self, *args, **kwargs):
        """ initialization of an BaseModel instance with attributes """
        if not (kwargs):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """ returns a str representation of a object """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """updates updated_at with current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns dict containing all key values of __dict__"""
        instance = self.__dict__.copy()
        instance['__class__'] = self.__class__.__name__
        instance['created_at'] = self.created_at.isoformat()
        instance['updated_at'] = self.updated_at.isoformat()
        return instance
