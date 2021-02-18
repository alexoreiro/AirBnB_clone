#!/usr/bin/python3
"""Console for Holberton HBNB project"""


import cmd
import json
import sys
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Contains de entry point of the HBNB console"""
    prompt = '(hbnb) '
    isClass = {"BaseModel", "User", "City", "Amenity",
               "Review", "State", "Place"}

    def do_quit(self, args):
        """Exits the program"""
        return True

    def do_EOF(self, args):
        """Exits the program"""
        return True

    def emptyline(self):
        """Doesn't execute anything when line is empty"""
        return False

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it to Json,\
        and prints the id"""
        argv = args.split()
        if len(argv) == 0:
            print("** class name missing **")
        elif argv[0] not in self.isClass:
            print("** class doesn't exist **")
        else:
            instance = eval("{}()".format(argv[0]))
            instance.save()
            print(instance.id)

    def do_show(self, args):
        """Prints the string representation of an instance, \
        based on the class name and id"""
        argv = args.split()
        if len(argv) == 0:
            print('** class name missing **')
        elif argv[0] not in self.isClass:
            print("** class doesn't exist **")
        elif len(argv) < 2:
            print("** instance id missing **")
        else:
            showme = storage.all()
            key = str(argv[0]) + '.' + str(argv[1])
            if key in showme:
                print(showme[key])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id,\
        but saves the changes in JSON file"""
        argv = args.split()
        if len(argv) == 0:
            print('** class name missing **')
        elif argv[0] not in self.isClass:
            print("** class doesn't exist **")
        elif len(argv) < 2:
            print("** instance id missing **")
        else:
            showme = storage.all()
            key = str(argv[0]) + '.' + str(argv[1])
            if key in showme:
                del showme[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        """Prints all str representation of all instances,\
        based or not on the class name"""
        argv = args.split()
        showme = storage.all()
        if (len(argv) == 0) or (argv[0] in self.isClass):
            print(showme)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding \
        or updating attribute, and saves the change in Json file"""
        argv = args.split()
        if len(argv) == 0:
            print("** class name missing **")
        elif argv[0] not in self.isClass:
            print("** class doesn't exist **")
        elif len(argv) == 1:
            print("** instance id missing **")
        elif len(argv) == 2:
            print("** attribute name missing **")
        elif len(argv) == 3:
            print("** value missing **")
        else:
            showme = storage.all()
            key = str(argv[0]) + '.' + str(argv[1])
            if key in showme:
                setattr(showme[key], argv[2], argv[3])
                storage.save()
            else:
                print("** no instance found **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
