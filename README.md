# 0x00. AirBnB clone - The console

![Image of Holberton B&B Logo](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/263/HBTN-hbnb-Final.png)

## Holberton School Airbnb Clone - Command Interpreter 

### 

This is the first of a multipart project working towards building a full web application clone of AirBnb. In this first part, the Python programming language is used to build a command interpreter for the clone's web app. This command interpreter is similar to a BASH shell but it is designed for a specific use case of managing objects related to this project. The following projects will incorporate additional sections like HTML/CSS templating, database storage, API and front-end integration.

The console can excute the following functions:
-   Create a new object (ex: a new User or a new Place)
-   Retrieve an object from a file, a database etc
-   Do operations on objects (count, compute stats, etc)
-   Update attributes of an object
-   Destroy an object

## Installation and Start

In the command line run ./console.py or echo help | ./console.py

Interactive Mode: How to ask for help:

PROMPT~$ ./console.py
(hbtn) help

Documented Commands (type help <topic>)
======================================
EOF   help   quit

(hbtn)
(hbtn)
(hbtn) quit
PROMPT~$

## Non-Interactive Mode:

PROMPT~$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
PROMPT~$ cat test_help
help
PROMPT~$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
PROMPT~$

Usage

This interpreter has basic console commands such as EOF, quit, help, create, destroy, update, show, count and all.

Command Sytax and Usage:
Command	Syntax	  Output
help	help *[option]*	Lists all available commands, or displays what option does
quit	quit Exit command interpreter
EOF	EOF  Exit command interpreter
create	create [class_name]	Creates an instance of class_name
update	update [class_name] [object_id] [update_key] [update_value]	Updates the key:value of class_name.object_id instance
show	show [class_name] [object_id]	Displays all attributes of class_name.object_id
all	all [class_name], all		Displays every instance of class_name, if used without option displays every instance saved to the file
destroy	destroy [class_name] [object_id] or	 Deletes all attributes of class_name.object_id
Files
File Name	Description
models/base_model.py	Base Class with public instance attributes and methods
models/amenity.py	An Amenity class that inherits from BaseModel
models/city.py		A City class that inherits from BaseModel
models/place.py		A Place class that inherits from BaseModel
models/review.py	A Review class that inherits from BaseModel
models/state.py		A State class that inherits from BaseModel
models/user.py		A User class that inherits from BaseModel
models/engine/file_storage.py  A class that serializes instances to a JSON file and deserializes JSON file to instances
tests/test_models/	       Unittests for BaseModel, User, amenity, city, place, review, state, and FileStorage



### Authors

* Pedro Arbilla | [GitHub](https://github.com/parbilla) 

* Alexis Oreiro | [GitHub](https://github.com/alexoreiro) 