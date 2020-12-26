---
name: Swing
tag: Languages
layout: page
---

A traditional java framework to create cross platform desktop GUIs.

---

Swing and AWT are GUI libraries in Java to create graphical user interfaces with which users interact with visual and audible feedback. 

The structure of such an application is split between: 

- Model. Consists of all the classes that represent the business logic of an application 
- UI . Part of the application that is attached to the model which handles the user and does not interact directly with the business logic 

The model and interface are sperate, but the interface can create instances of a model. Our UI will also control mouse and keyboard events. 

- AWT (abstract windowing toolkit) 
    - Older java UI framework  
    - Maps java code to OS specific UI framework 
- Swing 
    - Newer GUI library working with painting pixels directly 

At least three kinds of objects are needed to create a GUI in Java:  
- components  
- events  
- listeners 

A GUI could be created with these three general steps: 
- Populate a window with the necessary components 
- Define handlers to react to events in the interface 
- Define the relationship between these components and listeners 

## Components 
> An object with a visual representation 

A components position is relative to it's parent's, and specifies the top left corners location. Components can set their own visibility and status (enabled or disabled) 

## Containers 
> A component that can organize it's children components 

Either heavyweight (controlled by OS, more complex) or lightweight (Managed by Java) 

**Types of Container:** 

Frame 
- A container used to display a window, 
- Frames have a top level panel, this is the body of the window without the window frame 
- Return a `JFrame`'s panel with:

```
public Jpanel getContentPane() 
```

Panel 
- Top Level Containers 
- A container that can not be displayed without a parent container 
- All top level containers add components to a child panel. Such top level panel instances include: 
    - JFrame 
    - JWindow 
    - JDialog 
    - JApplet 

- Panels contain components 
- Default layouts for panels are FlowLayouts 

We should always add an additional panel to add a group of components 

## Layout Manager 
> Swing uses a layout manager to position elements automatically 
It is general practice to designate a whole class to a window and application components. 

**Types of Layout Manager:**

- `BorderLayout` - Splits view into five areas: North, West, East, South, Center. 
- `BoxLayout` - Stacks components on top of each other or in a row
- `CardLayout` - Manages components that share the same display space 
- `FlowLayout` - Places components in a row and then wraps when out of space 
- `GridBagLayout` - Displays in rows and columns of varying sizes 
- `GridLayout` - Displays in equally sized rows and columns 
- `GroupLayout` - Separates Horizontal and vertical layouts 


| Single Component | GridLayout or BorderLayout |
|---|---|
|Multiple components with natural size | Box or flow |
| Multiple components of the same size | Grid |
| Multiple components in a row or column with varying spacing  | Box |

## Events 
> GUI components respond to specific events (also an object) that occur during the runtime of a program.  

Some examples of events we may want to capture:  
- button clicks  
- selecting an item in a list  
- entering text in a field 

Events are all separate classes in java. An Events source is the object which triggered the event. Using events to develop a program is called Event-Driven.  

Common event interfaces are: 
- ActionEvent 
- WindowEvent 
- KeyEvent 

### Event Handlers 
> An event handler defines the behaviour once an event is triggered from the user interface 

A listener is an object that waits for an event and then handles it. Listeners are abstract 

Adapters are special classes that can implement only one of the abstract methods from an event handler. 

## Close Behaviours 

`EXIT_ON_CLOSE`:  
- Do not do anything when the user requests that the window close. Instead, the program should probably use a window listener that performs some other action in its windowClosing method.  

`DO_NOTHING_ON_CLOSE`:
- Hide the window when the user closes it. This removes the window from the screen but leaves it displayable.  

`HIDE_ON_CLOSE`:
- Hide and dispose of the window when the user closes it. This removes the window from the screen and frees up any resources used by it.  

`DISPOSE_ON_CLOSE`:
- Exit the application, using System.exit(0). This is recommended for applications only. If used within an applet, a SecurityException may be thrown. 

## MVC
> Model view controller architecture 
Model 
- Represents components data, its state 

View  
- Visual representation of component 
- Also responsible for sending events to the controller 

Controller 
- Processes data by reacting to input 

When one component is changed every model is updated 

[Top](#Java-Swing)