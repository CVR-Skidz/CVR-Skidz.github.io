---
name: Python
tag: Languages
layout: page
---

Python Language and library reference

*All \* represent optional arguments*

## Types

Primitive Data Types

| Bool  | Int  | Float (Double Precision) |
| ----- | ---- | ------------------------ |
| True  | 100  | 5e10 or 5e-10            |
| False | -100 | 1.1                      |

### Built-ins

A built in is an inbuilt method or object in the python language

| Signature         | Description                                                  |
| ------------------- | ------------------------------------------------------------ |
| `min([1], [n])`       | Returns the minimum value in the call. Any number of arguments can be passed |
| `max([1], [n])`       | Returns the  maximum value in the call. Any number of arguments can be passed |
| `round(x)`            | Rounds `x` to the nearest whole number                      |
| `abs(x)`              | Returns the absolute value of `x`                           |
| `pow(x, y)`          | Returns `x` to the  power of `y`                             |
| `type(x)`           | Returns the type  of `x`                                     |
| `isinstance(x,y)` | Returns `True` if `x`  is of type `y`, else `False`        |

### Casting

Casting is performed by placing the data to be casted inside a call to the output type.

```python
x = 4   # x is 4
str(x)  # x is "4"
list(x) # x is ["4"]
```

### Notes

- There are no constants in python
- Type does not regard inheritance, however `isinstance()` does



## Variables

### Scope
Global variables must be declared in a function's local scope to be accessible
```python
x = 0
def func():
	global x
	x = 1
	print(x)
```

### Built-ins

| Signature         | Description                           |
| ----------------- | ------------------------------------- |
| `del x`           | Deletes the reference to variable `x` |
| `None`            | None represents a `null` value        |
| `x, y = 10,  100` | `x` = `10` and `y` = `100`            |



## Conditional Statements

Conditional Statements requires data to be of the same type

| Syntax    | Description                                                  |
| --------- | ------------------------------------------------------------ |
| `if x:`   | Enter the scope of the statement if `x` is `True`            |
| `else:`   | Enter the scope of the statement if the previous statement was `False` |
| `elif x:` | Enter the scope of the statement if the previous statement was `False` and the condition `x` is `True` |

### Logical Operators

| Syntax    | Description                                      |
| --------- | ------------------------------------------------ |
| `x and y` | Results in `True` if both `x` and `y` are `True` |
| `x or y`  | Results in `True` if either `x` or `y` is `True` |
| `not x`   | Inverts the `bool` value of `x`                  |

### Comparison Operators

Comparison operators can be used on any type.

- `"A" > "Z"` : False (1 > 26)
- `"Jene" >  "Jerry"` : False (N < R)
- `True > False` : True (1 > 0)

### Truth Values

All objects evaluate to `True` unless their class defines a `bool` method returning `False`

| False                                    | True                             |
| ---------------------------------------- | -------------------------------- |
| `False`                                  | Custom objects                   |
| `None`                                   | Sequences with a length > 0      |
| `0`, `0.0`, `0j`                         | Sets or ranges with a length > 0 |
| `decimal(0)`                             | Numeric values != 0              |
| `fraction(0, x)`                         |                                  |
| Empty sequences `() or [] or {}`         |                                  |
| Empty sets or ranges `set() or range(0)` |                                  |

```python
'''Without one of the following overrides a custom object will evaluate to true'''

class Example:
	def __bool__(self):
		return False
		
    def __len__(self):
    	return 0
```

### Notes

- Python has no switch statement

- Pythons ternary operator appears as:

  ```python
  '''statement''' if '''condition''' else '''statment''' 
  ```



## Sequences

A class used to store multiple data pieces under one variable

### Instances of a Sequence

| List                                                         | Tuple                                                        |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| A collection of mutable elements in a changeable order.      | An immutable list, similar to an array.                      |
|```[ "element one", "element two", "element three" ] ```| ```{ "element one", "element two", "element three" }``` |

### Indexing
Indexes start from 0

| Index    | Element                                                      |
| -------- | ------------------------------------------------------------ |
| `s[1]`   | Access the second element of sequence `s`                    |
| `s[-1]`  | Access the last element of a sequence `s`                    |
| `s[1:3]` | Access the  elements of `s` up to but **not including** `s[3]` |

### Built-ins

| Signature                     | Description                                                  |
| ----------------------------- | ------------------------------------------------------------ |
| `len(x)`                      | Calculate length of `x`                                      |
| `range(start*,  stop, step*)` | Returns a `sequence` of numbers (of type `range`) in increments of `step` from `start` to `stop - 1` |
| `sorted(x, key*,  reverse*)`  | Returns a sorted copy of `x` in ascending order. Key is a transformation to apply to elements (`str.upper` converts all elements to upper case during sorting) |
| `any(x)`                      | Returns `True` if any elements in `x` can be evaluated to `True` |
| `all(x)`                      | Returns `True` if all elements in `x` can be evaluated to `True` |
| `min(x)`                      | Returns the minimum value in `x`                             |
| `max(x)`                      | Returns the maximum value in `x`                             |
| `sum(x)`                      | Returns the sum of all values in `x`                         |

### Strings

Strings are a sequence of Unicode characters **and not 8-bit ASCII values**

```python
"I am Unicode not ASCII!"
```

To convert a Unicode string to 8-bit values we must encode them with the correct character encoding.

```python
"I am Unicode not ASCII!".encode("utf-8") # [0x..., 0x..., 0x...]
```

### Bytes

Bytes are a sequence of 8-bit values, as such `strings` and `bytes` can not be concatenated.

```python
bytes([0x01, 0x02, 0x03])
```

To convert bytes to a string we must decode the byte values to the correct character encoding.

```python
bytes([0x45, 0x46, 0x47]).decode("utf-8") # "ABC"
```



## String Formatting

```python
"{0} {1}".format("Hello", "World!") # Hello World!
```

### String templates

String templates are a simple way of formatting strings with variable names.

```python
templateStr = Template("You are ${age}")
outputStr = templateStr.substitute(age=19)
print(outputStr) # You are 19
```

You can substitute into string templates using keys in a dictionary

```python
data = {"name" : "John Doe"}
templateStr = Template("Hello $(name)")
print(templateStr.substitute(data)) # Hello John Doe
```



## Iteration

Looping and incrementing

### For Loops

| Syntax                                 | Description                                                  |
| -------------------------------------- | ------------------------------------------------------------ |
| `for i in s`                           | Iterate through each element in sequence `s`                 |
| `for i in  range(start*, stop, step*)` | Iterate through each number from `start` to `stop - 1    ` in intervals of `step` |

### While Loops

| Syntax     | Description               |
| ---------- | ------------------------- |
| `while x:` | Loop until `x` is `False` |

### Built-ins

| Syntax         | Description                                                  |
| -------------- | ------------------------------------------------------------ |
| `break`        | Exits the scope of the loop                                  |
| `continue`     | Skips the rest of the scope for this iteration, skipping to the next iteration |
| `enumerate(x)` | Returns a collection's values mapped to their index i.e. the index followed by value. |
| `iter(x, y)`   | Returns the result of the call to `x` (something like `file.readline()`) until it matches `y` |
| `zip(x, y)`    | combines sequences `x` and `y`                               |

### Examples

```python
days = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
for i,d in enumerate(days):
	print(i, d)	# 1 Mo etc.
```

```python
file = open("test", "r")

'''read unti end of file''' 
for i in iter(file.readline(), ''):
	print(i)
```

```python
x, y = [1,2,3], ["one", "two", "three"]

for i in zip(x, y):
    print(i) # (1,"one")...
```

### Notes

- An iterable is anything that can be iterated through.



## Functions

| Syntax                         | Description                                                  |
| ------------------------------ | ------------------------------------------------------------ |
| `def method_name(x, y):`       | Function signature                                           |
| `return a + b` or `return a,b` | Return statement, multiple items can be returned             |
| `method_name()`                | Function call                                                |
| `method_name`                  | Function reference                                           |
| `def x(y = 1):`                | Assigns a default value to `y`                               |
| `def x(*args):`                | Defines a variadic  function with a variable number of arguments `args`. |

### Examples

```python
def x(*args):
	for i in args:
		print(i)
```

### Docstrings

Docstrings provide the documentation of a function to python, they are returned by `*functionName*.__doc__`

It is best practice to put a general description on line one of the docstring.

```python
def myFunction(arg1):
    '''myFunction(arg1) --> Example function
    
    Parameters:
    arg1: An argument
    '''
```

### Notes

- Functions will by default return a `None` value
- Functions are objects that can be passed to other code
- Functions can be called with parameters expressed by name rather than order.
  For example: `power(num=2, x=3)`. The order this is written in does not affect the call. 
- Variadic functions require the variable arguments to be declared as the last parameter.



## IO
### Output

| Syntax     | Description            |
| ---------- | ---------------------- |
| `print(x)` | Output `x` to `stdout` |

#### Streams

| Syntax        | Description                               |
| ------------- | ----------------------------------------- |
| `"w"  / "w+"` | Write modes                               |
| `"a"  / "a+"` | Append modes                              |
| `close()`     | Close a stream                            |
| `write(s)`    | Write a string `s`  to the stream         |
| `open(x, y)`  | Returns a stream  to path `x` in mode `y` |

#### Stream Members

| Member Name| Description       |
| ---- | ----------------------- |
| name | The  name of the file   |
| mode | The  mode of the stream |

### Input

|Syntax      | Description                                         |
| ---------- | --------------------------------------------------- |
| `input(x)` | Output `x` to  stdout and return input from *stdin* |

#### Streams

| Syntax        | Description                                                  |
| ------------- | ------------------------------------------------------------ |
| `"r"  / "r+"` | Read modes                                                   |
| `read(x*)`    | Returns the  contents of the stream or `x` characters from the seek pointer |
| `readlines()` | Returns the contents of each line in the stream              |
| `readline()`  | Returns the current lines contents                           |

### Seeking

Controlling the seek pointer in a stream

| Syntax    | Description                           |
| --------- | ------------------------------------- |
| `seek(x)` | Sets the seek pointer to position `x` |

### Iterating

```python
for line in open("test.txt", "r"):
    print(i.replace(1, 4)) 
```

| Test.txt              | Output                |
| --------------------- | --------------------- |
| 123<br />321<br />111 | 423<br />324<br />444 |



## Transforms

Transforms alter the contents of data

| Transform Function | Description                                                  |
| ------------------ | ------------------------------------------------------------ |
| `filter(x, y)`     | Calls `x` for each element in the sequence `y`, removing any indexes that return `False`. |
| `map(x, y)`        | Calls `x` for each element in the sequence `y`, replacing them with the result. |
| `sorted(x)`        | Sorts `x` in ascending order                                 |

```python
def filterFunc(x):
    if x.isupper():
        return True
    return False

list(filter(filterFunc, ["ABC", "abc"])) # ["ABC"]
```



## Objects

Objects are complex data types defined by classes

### Classes

A class is defined by the class signature. 

- To access anything in an instance of an object use `self….`
- To access anything belonging to the class use `classname….`

| Syntax                       | Description                                |
| ---------------------------- | ------------------------------------------ |
| `class x:`                   | Defines a class  `x`                       |
| `class x(y):`                | Defines a class  `x`, inheriting class `y` |
| `def  __init__(self, x, y):` | Defines a constructor                      |

### Function Members

All class functions must contain an argument self.

| Syntax             | Description                                       |
| ------------------ | ------------------------------------------------- |
| `def y(self,  x):` | Defines a member  function `y`.                   |
| `@staticmethod`    | Declares the following function as static         |
| `@classmethod`     | Declares the following function as a class method |

### Variable Members

| Syntax       | Description                                 |
| ------------ | ------------------------------------------- |
| `self.x = y` | Initialises an instance variable `x` to `y` |
| `name`       | Declares a public class variable `name`     |
| `_name`      | Declares a protected class variable `name`  |
| `__name`     | Declares a private class variable `name`    |

**NOTE:** Instance variables follow the same access modifiers



## Modules

Modules are external code sources.

| Syntax             | Description                  |
| ------------------ | ---------------------------- |
| `import x`         | Imports the module  `x`      |
| `from x  import y` | Imports `y` from  module `x` |
| `math.sqrt(9)` | Call the function  sqrt(x) from the module named math |

## Math

The `math` module

 ### Constants

- `pi`
- `e`
- `nan` (not a number)
- `inf` 

 ### Functions

| Syntax         | Description                                            |
| -------------- | ------------------------------------------------------ |
| `factorial(x)` | Returns the factorial of `x`                           |
| `sqrt(x)`      | Returns the square root of `x`                         |
| `gcd(x,  y)`   | Returns the greatest common denominator of `x` and `y` |
| `radians(x)`   | Converts `x` degrees to radians                        |
| `degrees(x)`   | Converts `x` radians to degrees                        |

### Trigonometry

| Syntax   | Description                       |
| -------- | --------------------------------- |
| `cos(x)` | Returns the cosine of `x` radians |
| `sin(x)` | Returns the sine of `x` radians   |

### Floats

| Syntax     | Description                        |
| ---------- | ---------------------------------- |
| `ceil(x)`  | Returns the next integer of `x`    |
| `floor(x)` | Returns the current integer of `x` |



## Random

The `random` module

 ### Functions

| Syntax                | Description                                  |
| --------------------- | -------------------------------------------- |
| `random()`            | Returns a random number between `0` and `1`  |
| `randomrange(x*,  y)` | Returns a random integer from `x` to `y - 1` |
| `sample(x,  y)`       | Return `y` random elements from `x`          |
| `choice(x)`           | Returns a random element from `x`            |
| `shuffle(x)`          | Sorts the elements `x` in a random way       |



## Statistics

The `statistics` module

 ### Functions

| Syntax        | Description                              |
| ------------- | ---------------------------------------- |
| `mean(x)`     | Returns the mean average of `x`          |
| `mode(x)`     | Returns the most frequent element of `x` |
| `median(x)`   | Returns the median element of `x`        |
| `variance(x)` | Returns the variance of `x`              |
| `stddev(x)`   | Returns the standard deviation of `x`    |



## Itertools

The `itertools` module: utility tools to iterate

### Functions

| Syntax                  | Description                                            |
| ----------------------- | ------------------------------------------------------ |
| `count(start*,  step*)` | Counts from `start` in `step` infinitely               |
| `cycle(x)`              | Infinitely iterates through `x`                        |
| `repeat(x)`             | Repeats `x` infinitely                                 |
| `permutations(x)`       | Returns all the possible orders of `x`                 |
| `combinations(x,  y)`   | Returns all possible combinations in `x` of length `y` |

 ### Examples

```python
for i in itertools.count(50):
    print(i) //	50,51,52,53...
```

```python
for i in itertools.cycle("HELLO"):
    print(i) // H,E,L,L,O,H,E,L,L,O…
```

```python
for i in itertools.repeat(1):
    print(i) // 1,1,1,1,1,1…
```

## Sys

The `sys` module: System utility

### Command Line

The sys module contains command line utilities

| Signature | Description                            |
| --------- | -------------------------------------- |
| argv      | The command line arguments in a `list` |



## Datetime

Datetime is a module containing classes for dates and times that can be subtracted, added, compared etc. as you would expect, where the corresponding members are mapped to one another. 

 ### Common classes

| Name        | Description                                |
| ----------- | ------------------------------------------ |
| `date`      | Date instances                             |
| `time`      | Time instances                             |
| `datetime`  | Datetime instances                         |
| `timedelta` | Used for  calculating  differences in time |

### Date

#### Function Members

| Signature     | Description                                        | Modifiers |
| ------------- | -------------------------------------------------- | --------- |
| `today()`     | Returns todays date                                | `static`  |
| `x.weekday()` | Returns a date `x`  as the day in the week (0 - 6) |           |

#### Variable Members

| Name    | Description           |
| ------- | --------------------- |
| `day`   | The day of the week   |
| `month` | The month of the year |
| `year`  | The dates year        |

 ### Datetime

#### Function Members

| Signature          | Description                                                  | Modifiers  |
| ------------------ | ------------------------------------------------------------ | ---------- |
| `now()`            | Returns todays date and time                                 | `static  ` |
| `time(x)`          | Returns the time of datetime `x`                             | `static`   |
| `strftime(f)`      | Returns a  formatted string of the time based on format specifiers in the string `f` |            |
| `fromtimestamp(x)` | Converts a timestamp to a datetime object                    | `static`   |

 ### Format specifiers

| Format | Description           |
| ------ | --------------------- |
| %y/%Y  | Year (19/2019)        |
| %a/%A  | Day name              |
| %d     | Day of the month      |
| %b/%B  | Full month name       |
| %c     | Locale datetime       |
| %x     | Locale date           |
| %X     | Locale time           |
| %I     | 12 hour time  (hours) |
| %H     | 24 hour time  (hours) |
| %M     | Minutes               |
| %S     | Seconds               |
| %p     | Am/pm                 |

### Timedelta

Time delta (`timedelta()` ) allows you to specify a point in time from today. 

#### Members

| Name     | Description  |
| -------- | ------------ |
| `days`   | Delta days   |
| `months` | Delta months |
| `years`  | Delta years  |



## Calendar

`calendar` is a module containing calendar date and time classes.

### Classes

| Name            | Description     |
| --------------- | --------------- |
| `TextCalendar ` | A text calendar |
| `HTMLCalendar ` | A html calendar |

### Function Members

| Signature                | Description                                                 | Modifier |
| ------------------------ | ----------------------------------------------------------- | -------- |
| `TextCalendar(x)  `      | Creates a calendar  from day `x`                            | `static` |
| `HTMLCalendar(x)  `      | Creates a calendar from day `x`                             | `static` |
| `monthcalendar(x,  y)  ` | Creates a calendar for the month  `y` in `x`                | `static` |
| `formatmonth(x, y)  `    | Returns a string  of the calendar in year `x` and month `y` |          |
| `itermonthdays(x,  y) `  | Returns the dates of each day in month `y` in year `x`      |          |

### Variable Members

Calendars are indexed data structures. `calendar.monthcalendar(2019, 2)[0]` returns the first week in February in 2019.

| Name         | Description                                          | Modifier |
| ------------ | ---------------------------------------------------- | -------- |
| `SUNDAY`     | Enumerator for Sunday, can be replaced with any day. | `static` |
| `month_name` | A sequence of  month names                           | `static` |
| `day_name`   | A sequence of day  names                             | `static` |

## OS

The `os` module includes utilities to interact with the operating system

### Path

Path is a class inside the `os` module that allows us to work with file paths

### Functions

| Signature        | Description                                                  |
| ---------------- | ------------------------------------------------------------ |
| `exists(x)  `    | Checks if the path  `x` exists                               |
| `isfile(x)  `    | Checks if the path  `x` is a file                            |
| `isdir(x)   `    | Checks if the path  `x` is a directory                       |
| `realpath(x)  `  | Returns the  absolute path to `x`                            |
| `split(x)  `     | Splits the file  and path of an absolute path `x` into a tuple |
| `rename(x, y)  ` | Renames `x` to `y`                                           |
| `getcwd()  `     | Returns the current working directory                        |

## Shutil

Shutil or shell utilities allows us to interact with the shell of the OS

### Functions

| Signature | Description |
| --------- | ----------- |
| `copy(x, y)`      | Copies `x` to `y` |
| `copystat(x, y)`  | Copies `x` to `y` retaining its metadata |

### Classes

| Signature                   | Description                                                  |
| --------------------------- | ------------------------------------------------------------ |
| `make_archive(x, y, z)	` | Creates an archive called `x` in format `y` (e.g. zip) containing the path `z` |

### Zip files
The module `zipfile` contains a class `ZipFile` with the following methods

| Signature | Description             |
| --------- | ----------------------- |
| write(x)  | Adds `x` to the archive |

## Web Data

Various ways to handle web data in python

### Requests
The `urllib.request` module contains the necessary methods to make a web request

| Function       | Description                                                 | Modifiers  |
| -------------- | ----------------------------------------------------------- | ---------- |
| `urlopen(x)  ` | Sends a request to the url `x`, returning a response object | `static  ` |

### HTTPResponse Object

| Member        | Description                               |
| ------------- | ----------------------------------------- |
| `getcode()  ` | Returns the  response code of the request |
| `  read()  `  | Returns the  contents of the response     |

### JSON

To interact with JSON we need the `json` module 

| Function      | Description                                                  |
| ------------- | ------------------------------------------------------------ |
| ` loads(x)  ` | Returns a python dictionary of the corresponding JSON object `x` |

### HTML

The module `html.parser` contains the `HTMLParser` class.

| Function      | Description                             |
| ------------- | --------------------------------------- |
| `  feed(x)  ` | Loads the parser with the html to parse |

 To process specific behaviour when reading html override the handle methods in a child class of `HTMLparser`.

| HTMLParser Functions                   | Description                           |
| -------------------------------------- | ------------------------------------- |
| `handle_starttag(self,  tag, attrs)  ` | Called on once a starting tag is read |
| `  handle_endtag(self,  tag)  `        | Called on once an ending tag is read  |
| `  handle_comment  `                   | Called on once a comment is read      |
| `  handle_data  `                      | Called upon reading a piece of data   |

### XML

The module `xml.dom.minidom` can be used to parse xml into buffered memory to manipulate the dom. The parser follows the standard dom methods, such as `getElementsByTagName` etc.

| Functions                     | Description                     |
| ----------------------------- | ------------------------------- |
| `  parse(x)  `                | Returns the parsed xml `x`      |
| `  getElementsByTagName(x)  ` | Returns the elements of tag `x` |