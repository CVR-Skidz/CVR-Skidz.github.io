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

Classes can inherit from other classes using parenthesis in the class signature:

```python
class DatabseConnection(Connection):
	pass
```

### Static Fields

Static varaibles are defined as regular fields in a class scope. For example the following is a static varaible to the StyleConfig class:

```python
class StyleConfig:
	background = "#333"

print(StyleConfig.background)
```

In python calling the attribute from a class reference (such as self) does not access the static attribute, but isntead an instance variable.

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
* Overriding methods requires no additional syntax, the child class automatically overrides any parent methods.
* `super()` returns the current object as an instance of the parent class (used within a class)

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

## Inheritence & Polymorphism

Classes in python can extend many classes, although this is frowned upon. We will stick to documenting single inheritence:

```python
class Connection(TCPEvent):
	pass
```

Connection is an instance of TCPEvent by inheritence, however python has no explicit interfaces so we can not implement an interface in the class signature to achieve this polymorphism. 

Interfaces and polymorphism is fulfilled by duck-typing: where an object is classified as an instance of a type based on the methods it defines, and not it's type. Hence strict interfaces don't exist and instead we just implement a set of methods in a class.

### Abstract Base Classes

> Using abstract classes to define an interface for duck-typing.

By using abstract classes we can define methods without implementations a class should provide, and is a way to add some guarantees to duck-typing. Abstract classes in Python are not an integral part of the language (such as Java or C++) and provide a module defining annotations and base classes to turn a regular class definition into an abstract class. This module is the `abc` module.

An abstract class uses decorators to define properties and methods a subclass must implement, as well as marking the actual class as abstract. The basic four patterns an abstract base class fulfills are:

1. The class has a metaclass of ABCMeta
2. Abstract properties (variables etc.) are decorated with the `abstractproperty` decorator, and have an empty body.
3. Abstract methods are decorated with the `abstractmethod` decorator, and have an empty body.
4. The class overrides a class method called `__subclasshook__` that returns true if the given class is a subclass of this, or false or NotImplemented if it is not.

```python
import abc

# define metaclass
class MediaContainer(metaclass=abc.ABCMeta):
	# file extension, subclass must implement this e.g. mp3, flac ...
	@abc.abstractproperty
	def extension:
		pass

	# abstract method, implement how to decode and play media in specified container
	@abc.abstractmethod
	def play:
		pass

	@classmethod
	def __subclasshook__(baseclass, subclass):
		# ensure baseclass is instance of MediaContainer, not a subclass
		if baseclass is MediaContainer:
			other_attributes = dir(subclass) #attributes of subclass
			
			# are the set of asbtract behaviours inplemented in the set of other attributes
			if set(baseclass.__abstractmethods__) <= set(other_attributes):
				return True

		return NotImplemented # is not a subclass, check if it is directly inherited (not duck-typing)
```			
			
## Exceptions

All exceptions in python inherit from the `BaseException` object. More specifically the standard library `Excpetion` inherits `BaseException`, common exceptions usually inherit from this class. Exceptions are raised with the `raise` keyword. If calling statements do not handle an excpetion it is raised (thrown) until something handles it, or the program terminates with an unhandled exception.

Exceptions can be handled in a try...except block. An except statement can optionally specify types of exceptions to catch, if none are specified any exception is caught. Multiple types of exceptions can be caught by delimiting them with commas:

```python
try:
	my_bad_function()
except (ZeroDivisionError, TypeError):
	print("There was a bad denominator or type")
```

Except statements can be stacked as well, only the first matching statement will execute. We can also reraise an exception in an except statement with raise.

```python
try:
	my_bad_function()
except ZeroDivisionError as e:
	print("Bad denominator", e)
except TypeError as e:
	print("Bad type", e)
	raise #reraise the type error
```

Adding an else statement to a try block executes when no exception occurs, and finally executes as you would expect, gauranteed after executing any other statement in the block. A finally clause still executes before a return statement in any other block.

> Directly inheriting from Excpetion is an efficient way to create exceptions.

```python
class MyException(Exception):
	pass
```


