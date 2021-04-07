---
layout: page
tag:
title: Python
---

Python language reference version 1.1 last revised April 2021.

## Modules & Packages

> Each python file is a module, a collection of modules in a directory can become a package.

Modules contain a local namespace and importing one module into another appends the entire namespace to the current local namespace. Meaning any modules imported by the second are included in the first. A modules name is defined by it's filename.

```python
# import database module namespace
import database

# import connection class from database namespace
from database import connection
```

Often we want to collect multiple modules into a package. A package is simply a directory of modules containing a `__init__.py` module. This module is executed when a package is first imported to a module. A common use for the package initializer is to move subpackage namespaces to the root of the package namespace. 

When a module is imported only code at a module level (global scope inside the module) is executed. Each module has a `__name__` variable listing the name of the current module when the given module was imported. When a module is executed without any active module (directly by the python interperater) this is set to `"__main__"`. 

```
- /
- main.py
- database/
  - __init__.py --> from connections import connection # allows: from database import connection 
  - db.py
  - connections/
    - __init__.py
    - connection.py
```

### Relative imports

Imports can be specified relatively or absolutely. When importing from the package name directly we call this an absolute import. However prefixing a package namespace with `.` allows us to traverse up a hierarchy of pacakges - a relative import. A single prefix specifies an import relative to the current package, and multiple prefixes traverses up parent packages.

We can import the connection module with:

```python
from database.connections import connection
```

From inside the db module we could use a relative import: 

```python 
from .connections import connection
```

Similarly from inside the connection module we could import the db module with 

```python
import ..db
``` 

## Classes

Classes are defined with the `class` keyword and have both a contructor `__new__` and intializer `__init__`. The constructor is rarely used as each function is responsible for:

* intializer: Intialize the class state
* contructor: Allocate memory and return the object

As such only specialized classes will define a specific constructor. The constructor can not take any additional arguments.

* Classes are instantiated by calling the class name, such as `conn = Connection()`.
* Classes do not require attributes to be pre-declared, and can be assigned directly to the object reference using dot notation.
* If a class attribute is accessed without being initialized an `AttributeError` is raised.

```python
# instantiate a connection
conn = Connection()

# the connection instance conn now has an attribute named target
conn.target = "db.host.xyz" 

print(conn.target) # ok
print(conn.user) # AttributeError exception
```

### Class Methods

Methods are defined just as a function would be, but all require a mandatory argument. Each method is passed a reference to the instance the method was invoked on, by convention this is called `self` although technically whatever the first argument is called will be assigned the reference. This argument is not passed by the caller however:

```python
class Connection:
  def __init__(self, target):
    self.target = target

  def login(self, user):
    self.user = user

conn = new Connection("db.host.xyz")
conn.login("admin")
```

* Methods can define default values for arguments with a trailing `=`.

### Docstrings

Including a string as the first statement in a method is known as a docstring, and documents the usage of a method. These can be single or multiline strings. Calling `help(Class)` will print all the docstrings for that class.

### PEP OOP Conventions

> PEP (Python enhancement proposal) defines conventions for object-oriented python, as the language itself tries not to enforce strict rules on users.

* Classes be named in CamelCase
* Methods avoid using both leading and trailing underscores, such as `__MyMethod__`

### Encapsulation

Python does not enforce any kind of encapsualtion, everything is therefore public. Again python uses PEP to suggest convetions, and these are strongly followed. PEP suggests that any field prefixed with a single underscore only be called internally (privately) or under circumstances when a user has no other options. As such external calls to such fields are almost never seen. To take things a step further we can name mangle fields by prefixing the name wiht two underscores, this reqwrites the name for external calls but leaves it unmangled internally. This is very rare, and usually discouraged as a single prefix is treated as a protected field.

* Name mangling prefixes a field name with `_<classname>.` externally

```python
class Connection:
  class Connection:
  def __init__(self, target, user):
    self.target = target
    self.user = user
    self._login()

  def _login(self):
    print(self.user, "logged in")

  def __logout(self):
    print(self.user, "logged out")

conn = Connection("db.host.xyz", "admin")
conn._login() # discouraged, protected
conn.__logout() # error
conn._Connection.__logout() # must unmangle name, but even further discouraged
```

