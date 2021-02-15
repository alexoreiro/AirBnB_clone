#!/usr/bin/python3
""" Create a Filestorage instance storage """

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
