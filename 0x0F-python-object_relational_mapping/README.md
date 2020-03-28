# 0x0F. Python - Object-relational mapping

## Requirements

### General

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
- Your files will be executed with MySQLdb version 1.3.x
- Your files will be executed with SQLAlchemy version 1.2.x
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7.*)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- You are not allowed to use execute with sqlalchemy

### More Info

Install MySQLdb module version 1.3.x

For installing MySQLdb, you need to have MySQL installed: How to install MySQL 5.7 in Ubuntu 14.04
```
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient==1.3.10
...
$ python3
>>> import MySQLdb
>>> MySQLdb.__version__ 
'1.3.10'
```

Install SQLAlchemy module version 1.2.x
```
$ pip3 install SQLAlchemy==1.2.5
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.2.5'
Also, you can have this warming message:

/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be re
moved in a future release.")                                                                                                                    
  cursor.execute(statement, parameters)  
```

    You can ignore it.
