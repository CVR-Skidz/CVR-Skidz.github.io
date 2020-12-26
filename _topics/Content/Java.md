---
name: Java
tag: Languages
layout: page
---

Language reference for the Java programming language. 

- For GUI programming using java see [here](./Swing.md).
- For notes on the Java Collections Framework [here](./JCF.md)

## Types
> Each type in java is either a class, interface, primitive, or array. 
 
Types can either be a primitive (int, char etc.) or a reference (pointer) to an object. Interfaces declare the methods defining an objects behaviour. The declared methods are defined in a class that implements  the interface. Types can be cast or promoted, promotion will truncate values.
{% highlight java %}
(float) 10/2;       //2.5
float res = 10/2;   //2.0 
{% endhighlight %}

### Primitive Types
> Primitives start with a lower case letter, of which there are 8. 

- int - 32 bit number 
- short - 16 bit number 
- long - 64 bit number 
- char - unicode character 
- boolean - `true` or `false` 
- byte - 8 bit number 
- double - Floating point number taking double the space of a float in memory
- float - Floating point number

 Primitive types can only be passed by value, to pass by reference or convert between complex types use a wrapper such as Integer. Wrappers are classes that automatically pack or unpack primitive types. Hence `test(int x)` will accept `new Integer(4)`. 

## Arrays
> Consecutive spans of memory designated to holding a certain type of data. Indexable.

A variable set equal to an array object contain a reference to the array. Arrays must be initialized by creating a `new type[length] {values}` array. 

Values in arrays will have default values. Arrays have a length member. 


Implicit:

{% highlight java %}
new int[] {1,2,3,4,5}; 
{% endhighlight %}

Explicit 

{% highlight java %}
new int[5]; 
{% endhighlight %}
 
### Multi Dimensional Arrays 
> Arrays which contain "sub-arrays", i.e. an array of arrays

Multi dimensional arrays use multiple `[]` to declare dimensions. In a multi dimensional array the length of an unspecified dimension will return the array length of the first element 
- `grid.length` gives `2` (the same as `grid[0].length`) 

{% highlight java %}
{% raw %}

int[][] grid = new int[][] {{1,2},{3,4,5}} 
grid[0][1] //2 

int[][] grid = new int[2][3] 
grid[0][1] //2 
{% endraw %}
{% endhighlight %}

## Casting
> Casting explicitly converts type - allowing the truncation of data. 

- Implicitly converting types will not truncate data, and therefore if types possibly do cause data loss will cause a compiler error. 

- Promotion is the automatic casting of data where two operands differ in type. The smaller operand (type size) will be promoted to the bigger. 
 
Up casting is the promotion or cast of a child class to a parent class. Down casting is the cast of a parent class to a child class (can not promote) 

Casting does not change object data only reference types, you can not cast a parent object to a child object you can however cast a parent reference to child reference that's object is of the child type. 

## Generics
> A generic allows the implementation of an interface or class without being type specific.

Generics are a concept related to generic programming. This allows general behaviour on any data type passed as a generic. 

For instance `ArrayList<T>` defines a generic `T`, allowing the list to be implemented over any type. The type of elements in an `ArrayList` is irrelevant for it's implementation.

To pass a value of any generic we can use a wildcard testMethod(ArrayList<?> value). You can only access data defined in the ArrayList interface in this case. You can however use: testMethod(ArrayList<? extends yourClass> value) and inherit a specific class. 

## Encapsulation
> Encapsulation protects the scope of a class and exposes functions by endpoints in an API 
 
- This prevents people worrying over how the class works and just what it can do.  
- An object instance data should only be able to modified by that object. 
- Through this we should define getters (accessors) and setters (mutators). 
- Fields that do not change state are immutable 

### Access modifiers 

| public  | private  | protected |
|---|---|---|
| Accessed anywhere in an application | Accessed within the class it is declared | Accessed by the declared class, any sub-classes, and the same package. |

## Objects

Objects in Java have a state (fields/members) and a behaviour (methods). Instances are allocated to the heap, and do not contain an object but a pointer to one - called a reference 
 
Objects are the result of a Class, and are instantiated with a Constructor, Constructors have the following signature `[accessor] [name] ([arguments]])` 
- Constructors can not be static 
 
Files that define a class must be named the same as the class.
- `==` will compare the reference of an object, not the state. Use `equals(x, y)` for the later.
 
Objects can only inherit one parent class, only objects can be instantiated (not interfaces etc.).

All methods in an object can be overloaded (changing the signature of a method to provide an additional method) and overridden (Changing the body of an inherited method to provide specific behaviour).

Variables assigned to objects are given a reference to the object in memory. The type of the variable can be casted to change the interface of the object, however the underlying instance **is not** mutated. 

**Memory is only allocated once an object is defined (instantiated).**

- Objects are passed by reference. Except `String`(s).

## Classes
> Classes are structures that can be instantiated to create an object

Classes define the interface or behaviour (or both) of an object. Traditional classes (concrete classes) define both the interface and behaviour of an object, and can be inherited or inherit other classes, as well as implementing an interface.

- Classes can only inherit one parent (super) class.
- One java source file can only have one public class.
- One java source file can contain many protected or private classes.

| Accessibility | Class | package | Subclass | World |
|---|---|---|---|---|
| `public` | T | T| T |T |
| `proteted` | T | T | T | F|
| `default` | T | T | F| F |
| `private` | T | F | F | F| 


### Abstract Classes 
> Abstract classes declare general behaviour to be inherited by a sub class. 

- Usually represent something intangible 
- Abstract classes cannot be instantiated, but can be a reference type 
- Declares but does not define behaviour associated with abstract methods, this is the responsibility of any class that inherits the abstract class. 
- Abstract classes can also contain abstract methods, whilst non-abstract classes can not.

{% highlight java %}
myAbstractClass = new myConcreteClass() //valid
myAbstractClass = new myAbstractClass() //invalid
{% endhighlight %} 
**NOTE:** Abstract classes can still contain all a normal class can, but anything declared as abstract within it can have no body 
 
### Anonymous Classes 
> Anonymous classes are instances of a class where their behaviour is overridden at instantiation. 

{% highlight java %}
/* 
    AN ANONYMOUS CLASS EXAMPLE 
*/
Machine camera = new Machine() { 
        @Override public void start(){ 
            System.out.println("Camera Started"); 
        } 
} 
{% endhighlight %}

## Polymorphism
> Polymorphism allows the use of child classes in place of parent classes 
 
Through inheritance, classes can contain parent and child classes. Casting either object between one another is known as polymorphism.

- Allows overriding (abstract) method definitions
- Inheritance is only one way 

Casting a parent to child class is known as down casting, casting a child to parent is known as up casting. 
 
Allows: 
- Code reuse 
- Eliminates redundancy 
- Generic programming 

{% highlight java %}
private class Number extends Integer{
    public square() {
        return this * this;
    }    
}

private static intFunc(int n) { 
    System.out.println(n); 
    n.square(); //error int has no method square    
}

//...
Number n = 7;
intFun(n); //upcasting
{% endhighlight %}

- Static methods cannot be overridden.

## Interfaces
> Interfaces allow us to define shared method signatures between classes not directly related. E.g. the classes do not share a common parent etc. 
 
Interfaces do not contain definitions, they exist to tell us that objects implementing the interface will contain a method of the same signature (to allow us to use the same methods) with unique functionality. 
 
- Interfaces can allow you to pass objects to methods with different types. 
- An interface only has method-signatures 
 
{% highlight java %}
public interface MyInterface {}
public class MyClass extends MyParent implements MyInterface {} 
{% endhighlight %}

- Interface methods need to be public 
- A class can implement multiple interfaces 
{% highlight java %}
public class [...] implements Int1, Int2, Int3 ... 
{% endhighlight %}
 
## Collections
> A collection is an object that gathers and organises a group of objects (called elements). 

A Collection is a type of interface to give a general methods for all groupings of data, with specific functionality based on the type of data structure desired.

- Collections have an abstract data type (ADT)  
- Describes methods used to access and manipulate data in the collection. 

Collections use a data structure to store and manipulate data. Beneath this are algorithms used to search, set, get etc. 

## Hash Maps & Sets
> Performant unordered collections that split data into multiple collections identified by a hash, providing constant time operations.

**HashMap** 
- Implements Map 
- Maps keys to values 
- Unordered, the order is not guaranteed 
- Values are stored in a collection 
- Keys are stored in a HashSet 
{% highlight java %}
HashMap<K,V> 
{% endhighlight %}
- `put(K, V)` adds a new key and value to the map 
- `get(K)` returns the related V value from the collection of values 
- Key-value pairs are stored in an object called `Entry<K, V>` 

The HashMap contains a set for keys and entries, as well as a collection for values.

**HashSet** 
- Implements Set 
- Contains no duplicate items 
- Items have no indices (unordered) 
- Items do not shift (removing the first element will not move the second down) 
{% highlight java %}
HashSet<T> 
{% endhighlight %}
- `add(T)` does not add elements in a specific position 
- If the item already exists in the set `add()` returns false 
- Sets can not access indices, therefore we can not use a for loop to access elements 

## Packages
> A package is a namespace for related classes. These classes provide functionality (similar to a library). 
 
When providing classes for a package the package is declared first, then any imported packages used to provide functionality are listed. This precedes the definition of any class.

{% highlight java %}
package mypackage; //declare package
import anotherpackage; //import package
{% endhighlight %} 

Packages collect java files into one group. Packages are unaware of other packages unless imported. i.e I can create a test package and an application package both with main methods, only the one I am using (run/compile from) will run. This is the same with sub packages. 

## Exceptions
> An Exception is an object, when it is thrown Java will look for something to handle the exception. an unhandled exception will either break the program at runtime, or prevent successfully compiling. 

Exceptions are thrown and can be caught to handle them. Throwing an exception will break out of the scope of a method. Catching an exception can be used in a try - catch block. This will not break the scope. 
 
Where it is possible to throw different exceptions you must declare 
{% highlight java %} 
[method signature] throws [exception 1], [exception 2]
{% endhighlight %}

To catch multiple exceptions we use a multi catch. 
{% highlight java %}
try {
    //...
}
catch([exception 1] a | [exception 2] b) {
    //...
}
{% endhighlight %} 

To throw an exception at a specific point in code we throw a new exception
{% highlight java %}
throw new IOException("Error message"); //example
{% endhighlight %}
**General Rules:** 
- Exceptions should not be caused by the programmer, and we should not try to handle these 
- Exceptions should be handled from user input, or an unpredictable event 
- Checked exceptions will stop compilation 
- Unchecked exceptions (Such as errors or runtime exceptions) will not stop compilation and cause errors when running the program 


Methods that have unchecked exceptions automatically throw the exception, in the calling method it will also need to throw this exception if it does not want to handle it. 

## Streams
> Sequence of data to be read in the form of binary digits. 

Streams can be written to and read from. There are two types of streams:

- Data streams deal directly with the sources of data 
- Filtering streams manipulate data into a more useful form 

Input streams read data into a program, whilst output streams write data from a program to a destination. 

In general Unicode text streams are children of `Reader` and `Writer`. Whereas `InputStream` and `OutputStream` are byte-oriented streams.
 
## File I/O
> File I/O allows persistent storage of data 

Non-Buffered I/O writes each bit/byte as soon as possible and introduces some overhead for each byte. Buffered I/O on the other hands stores data and then writes "chunks" to disk.

- Text Files: Bits are represented as printable characters. e.g. "1" or "A".
- Binary Files: Bits represent encoded information. e.g. "01111111".

### Writing

- `FileWriter`: non-buffered I/O
- `BufferedWriter`: buffered I/O
- `PrintWriter`: buffered I/O

### Reading

- `FileReader`: non-buffered I/O
- `BufferedReader`: buffered I/O
- `StringTokenizer`: token I/O (reading strings between delimiters)

## The Final Modifier 
> Classes, methods, variables, and references can be final 

A final:
- Class can not be inherited
- Methods can not be overridden
- Variables can only be initialised
- References can not point to another object

## Class Design
> Determining classes that contribute to the program, and designing them.

Using linguistic analysis, nouns are generally objects unless they are clearly primitive. When an attribute is too complex to be a primitive, it is therefor a class.

Classes can relate to on another, as described below:

|Relationship|Description|
|---|---|
|Association|Class `x` uses `y` in some way|
|Aggregation|Class `x` has a `y`|
|Composition|Class `x` exists as long as it has a `y`|
|Inheritance|Class `y` is an extension of `x`|

- If a `has a` relationship is a composition the member of the composed class is usually marked `final`.

**A class should only represent a single entity, with a set of similar operations.**

## SOLID OO Design
> An object oriented design methodology

- (S)ingle responsibility. A class should focus on doing only one thing.
- (O)pen-closed principle. Each object should be able to be extended without affecting existing implementations, and after adding new functionality we should not modify the original implementation.
- (L)iskov substitution principle. Subclasses must be able to substitute base types without breaking functionality. A subclass must satisfy the constraints of a base class. 
- (I)nterface segregation. Clients should not be forced to rely on an interfaces they do not use.
- (D)ependency inversion. High level models should depend on low level models, both should depends on abstract classes or interfaces.

## Multi Threading
> Intercommunication between threads

When a process is run by a processor it is assigned a self-contained execution environment and its own runtime resources. Threads share all the resources allocated to a process, because of this a thread requires less resources than a process.

In java to create a thread we must create an object containing the task to run in the thread, as well as a `Thread` object itself. We can use the `Runnable` interface to create such a task. 

{% highlight java %}
void myTask() { ... }

Runnable task = this::myTask;
Thread thread = new Thread(task);
thread.start();
{% endhighlight %}

`Thread`(s) start method is marked as `native` which specifies the method is implemented in the JVM not JDK (running machine compliable code). Hence the thread is started by a native instruction in the JVM. The scheduler will run a thread if its state is runnable.

- A threads state can change to blocked, sleeping, waiting, or dead.
- The scheduler will run threads based on their priority (1-10, higher -> more priority). A higher priority has a higher probability to run.

We can stop (set its state to runnable from running) the currently executing thread with `yeild`. We can **block** (set its state to blocked from running) it temporarily with `sleep`. Additionally we can interrupt a thread, this is an indication to the thread to stop what it is doing and run something else. 

Before a thread is scheduled by the processor we can call `join` which will wait a certain amount of time before starting another thread. A value of zero means to wait until the thread is finished.


## Java Database Connectivity

The java database connectivity (JDBC) is a common API for databases to implement to allow java applications to connect to many DBMS (Oracle, MySQL etc.). It provides methods to execute SQL commands (CRUD). The JDBC is contained within `java.sql`, using it requires:

- A database driver (as a `jar`)
- Establishing a connection

The `DriverManager` class can be used to establish a connection to a database. To use a database that is integrated as part of the application we can run a database in embedded mode. From a database connection we can create and execute SQL statements, as well as query database metadata.

## Design Patterns
> A general reusable solution to a commonly occurring problem. A description of a solution to be used in many situation.

Patterns are can be thought of as a problem and solution pair, patterns occur at three levels:

- Code level (idioms: a common practice, algorithm, or data structure)
- Subsystem level (design patterns)
- System level (architectural styles)

There are mainly three types of design patterns (subsystem level):

|Design pattern type|Description|
|---|---|
|Creational| Object creation mechanisms|
|Structural|Organising objects to form larger structures providing new functionality, identifying a simple way to realize the relationship between entities|
|Behavioural|Realizing common communication patterns between objects|

### Creational Patterns
> Object Creation Mechanisms 

- **Factory** patterns facilitate the creation of sub classes when the number of sub classes is large enough to introduce complexity by providing a separate class capable of creating sub classes based off input.
- **Singleton** patterns limit the instances of an object within a *running program* to **one** to provide a centralised point to manage internal data. 
  - This is achieved by creating a default private constructor, then making available a synchronized public method to access a reference to the static instance (the object we are limiting). Additionally the `clone` method needs to be overridden to disable it.
- **Adapter** patterns allow unrelated interfaces to work together. By providing an additional class we can perform operations to make the input for one class compatible with another, to produce the intended output.  
- **Mediator** patterns allow multiple loosely coupled classes to be maintained easily. Only one class (the mediator) is aware of all the coupled objects, and each of these objects only interact with the mediator. This allows each class to only focus on their isolated responsibilities.

### Architectural Styles 
> Organizing components of a program, and how they interact with each other.

#### MVC
> Architectural style separating components into a model, view, and controller.

MVC styles firstly separate the UI and model (program logic). The UI is then further separated into view (displaying information) and controller (processing input).

- Model: Data and rules governing the access to and updates of this data. 
- View: Rendering the content of the model. 
- Controller: Translates interactions from the view to processes for the model to execute.

The general pattern is: The `view` displays data > The `controller` captures input > The `model` updates data and notifies the `view`.

## Testing
> Verifying software against use cases either manually or automatically.

Human errors that create incorrect results are seen as mistakes. These mistakes lead to software faults (bugs) that create failures (incorrect results, outputs etc.). As developers we **verify** there are no faults, and **validate** the software meets requirements.

Verification can be accomplished by:

- Testing (demonstrating correct behaviour over multiple cases)
- Formal verification (proving the underlying algorithm)

Developers perform unit and integration testing (low-level). Usually system, usability, performance, and stress testing id performed by a testing group. Unit testing tests components in isolation to identify the location of a fault whereas integration testing combines and tests multiple components to discover interface errors. 

Tests can be:

- Black-box: comparing the input and output (no internals).
- White-box: evaluating the structure of code.

Flow graphs can be used to identify the steps present when performing white-box testing. One a flow graph is created a test should be created for each edge. 

### Unit Testing

Unit tests pass or fail components by using black-box testing. In java `JUnit` is a common unit testing framework.

`JUnit` tests are methods created with the `@Test` tag, that contain an `Assertion` to pass or fail the input and output. If an assertion is true the test continues, otherwise it exits prematurely. If a test completes it will pass, otherwise it will fail. The `Assert` class provides:

- `assertEquals` to check if input matches output
- `assertTrue` to check if input is true
- `assertFalse` to check if input is false
- And more ...

Any context required for a test to run is provided by a test fixture. Using the `@Before` tag will ensure a method is called before each test case, whilst `@After` does the opposite. `@BeforeClass` will ensure a method is called when the class is created, and `@AfterClass` runs only once after all test cases are completed. 

## Code Smells
> Symptoms of poor program design

Code smells can be trivial or severe, and represent poor design that impedes the maintainability and readability of code. Some common trivial code smells include:

- Dead code: Code that is no longer used by the system
- Meaningless variable names
- Inappropriate indenting

To remove code smells we can refactor. Refactoring is the discipline of altering existing code structure without changing external behaviour.

### Code Smell - Bloaters

Code that has increased to huge proportions over time that make it difficult to deal with. Often bloaters can be identified by:

- Long methods: excessively long methods can be refactored into a different class.
- Long classes: huge classes can be refactored by extracting smaller classes categorized by the many functions the original class is responsible for. 
- Data clumps: large groups of variables shared throughout a program should be encapsulated into their own class. 

### Code Smell Object Orientation Abuse 

Idioms that are not coherent with OOP are called abusers. Common examples include:

- Inappropriate switch statements: using switch statements to change the output of a method is better resolved by using polymorphism and overriding the method for a specific child class.
- Unrelated inheritance: creating a child class that only inherits specific behaviour from a parent to provide code reuse often causes an inconsistent interface to that object and can cause errors. For example if an animal super was extended by a class "Chair" only because an animal has "legs".
- Change preventers: highly coupled classes that mean when you change one class or add a feature we must modify many other classes as well.

> Coupling is the degree of interdependence modules have with one another. How closely connected two modules are. The opposite of coupling is cohesion, if a class has low coupling it will have high cohesion and is considered well-structured. 

[Top](#Java)