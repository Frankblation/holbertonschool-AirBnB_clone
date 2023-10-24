
# AirBnB clone - The Console // cmd

## Introduction

* This is a collaborative project to build a clone of a previous version of the AirBnB website. 

* This project utilizes a console, which is a command interpreter, similar to a shell, that manages python objects
    and their storage. The following image depicts the stage of the ongoing project:

![image](https://github.com/allisonabinger/holbertonschool-AirBnB_clone/assets/127708538/0a52936e-8a13-42bc-934e-97ca2133ed44)

* The Console follows CRUD (Create, Read, Update, Delete) // 

    * creates a new objects
    * retrieves an object from a file
    * update/operate on the objects
    * destroy an object

    * More on CRUD: <https://www.sumologic.com/glossary/crud/#:~:text=CRUD%20is%20an%20acronym%20that,%2C%20read%2C%20update%20and%20delete.>

* This program is designed to create, read, manipulate, and delete objects under the theme of AirBnb. The following classes exist as objects to create:
	- Base: The base model for the following classes.
	- User: Includes first name, last name, email, and password.
	- Place: Includes city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, amenity_ids
	- Review: Includes place id, user id, and text.
	- State: Includes name
	- City: Includes state ID and name.
	- Amenity: Includes name.


## Usage

The console can be started by running the ./console.py module, which will open a command-line interpreter tool. Here is what the console looks like:


The console can be used in interactive and non-interactive mode:

In interactive mode

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

in Non-interactive mode

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```


## Storage

Filestorage handles the storage engine for all classes. 

## Testing

All tests are done in 'unittest' format inside the /tests directory. An example of a test is as follows:




## Available Commands

Running the help command will give a list of the available options inside the console:

<img width="560" alt="Help" src="https://github.com/allisonabinger/holbertonschool-AirBnB_clone/assets/127708538/f05c6196-d700-4e97-b54d-4d647a31fb37">


* Create

> *Creates a new instance of a given class. The class' ID is printed and the instance is saved to the file file.json located in the repository.*

```bash
create <class>

```

```bash
(hbnb) create BaseModel
4d5b16f9-3cd1-49d3-b44c-9e9d4a42d1c0
(hbnb)
```

* Show

```bash
show <class> <id>
```

```bash
(hbnb) show BaseModel 4d5b16f9-3cd1-49d3-b44c-9e9d4a42d1c0
[BaseModel] (a) [BaseModel] (4d5b16f9-3cd1-49d3-b44c-9e9d4a42d1c0) {'id': '4d5b16f9-3cd1-49d3-b44c-9e9d4a42d1c0', 'created_at': datetime.datetime(2021, 11, 14, 3, 28, 45, 571360), 'updated_at': datetime.datetime(2021, 11, 14, 3, 28, 45, 571389)}
(hbnb)
```

* Destroy

> *Deletes an instance of a given class with a given ID.*
> *Update the file.json*

```bash
(hbnb) create User
14cc2730-8e1a-4cb3-9e47-d6a2b4adca47
(hbnb) destroy User 14cc2730-8e1a-4cb3-9e47-d6a2b4adca47
(hbnb) show User 14cc2730-8e1a-4cb3-9e47-d6a2b4adca47
** no instance found **
(hbnb)
```

* all

> *Prints all string representation of all instances of a given class.*
> *If no class is passed, all classes are printed.*

```bash
(hbnb) create BaseModel
c3d2c80e-8b5f-4d6c-90da-5f9d542b96a6
(hbnb) all BaseModel
["[BaseModel] (c3d2c80e-8b5f-4d6c-90da-5f9d542b96a6) [BaseModel] (c3d2c80e-8b5f-4d6c-90da-5f9d542b96a67) {'id': '4c3d2c80e-8b5f-4d6c-90da-5f9d542b96a6', 'created_at': datetime.datetime(2021, 11, 13, 22, 19, 19, 447155), 'updated_at': datetime.datetime(2021, 11, 13, 22, 19, 19, 447257), 'name': 'My First Model', 'my_number': 89}"]
["[BaseMode
```

* count

> *Prints the number of instances of a given class.*

```bash
(hbnb) create City
c3d2c80e-8b5f-4d6c-90da-5f9d542b96a6
(hbnb) create City
e95234772-83a5-41e9-b728-6bc2345c21b4
(hbnb) count City
2
(hbnb)
```

* update

> *Updates an instance based on the class name, id, and kwargs passed.*
> *Update the file.json*
```
```
# Authors
Allison A Binger:
	github.com/allisonabinger
Frank Blation
	github.com/Frankblation
