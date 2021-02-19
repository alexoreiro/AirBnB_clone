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
        """Prints string representation of all instances of a given class,\
        if no class is specified, prints all instances"""
        argv = args.split()
        showme = storage.all()
        if (len(argv) == 0) or (argv[0] in self.isClass):
            inst_list = []
            for obj in showme.values():
                if len(argv) > 0 and argv[0] == obj.__class__.__name__:
                    inst_list.append(obj.__str__())
                elif len(argv) == 0:
                    inst_list.append(obj.__str__())
            print(inst_list)
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

    def do_count(self, args):
        """Retrieves the number of instances of a class"""
        cont = 0
        argv = args.split()
        showme = storage.all()
        for obj in showme.values():
            if argv[0] == obj.__class__.__name__:
                cont += 1
        print(cont)

    def default(self, args):
        """For when you call Class.command"""
        for char in args:
            if char == '(':
                args.replace("(", ".(")
        try:
            argv = args.split('.')
            if argv[0] in self.isClass:
                if argv[1] == 'all':
                    self.do_all(argv[0])
                elif argv[1] == 'count':
                    self.do_count(argv[0])
        except:
            pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
