# Class

Python is an object oriented programming language.

An object is an collection of three basic characteristics. These are Identity, State, and Behaviour.

Identity:
    * An object has its own identifier and can be differentiated from all other objects.
State: 
    * Properties of an object
    * An object can have variables to store data
Behaviour:
    * Actions that an object can take
    * An object can have functions that can be called.

A class is an object constructor. It can be thought of as a blueprint for creating an object.

## Creating a class

A `class` is defined using the `class` keyword

```python

class Person:
    name = "Bob"
    age = 21
```

Here we have created a class that will be used to create an object of a person.

## Creating an object

Now we have a class, we can create an object.

```python

person1 = Person()
print(person1.name) # Will print: "test"
print(person1.age) # Will print: 21

```

## __init__() function

The above example is a class in the most basic form. These arn't very useful, but we can use the __init__ function to expand on this.

All classes have a __init__() function, which is executed when a class is used to create an object. If you do not define one, it still runs but is effectively empty and doesn't do anything.

You can use a __init__() function to assign values to an objects properties, or perform action necessary when being created.

```python

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person(name="Bob", age=21)
print(person1.name) # Will print: "Bob"
print(person1.age) # Will print: 21

person2 = Person(name="Billy", age=50)
print(person2.name) # Will print: "Billy"
print(person2.age) # Will print: 50
```

Here we create two person objects, and assign them a name and age dynamically.

# Object functions

A class can have functions defined, so you can interact with an object in defined ways.

```python

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayHello(self):
        print("Hello, my name is " + self.name)

    def sayAge(self):
        print("My age is " + self.age)

    def birthday(self)
        self.age = self.age + 1

person1 = Person(name="Bob", age=21)
person1.sayHello() # Will print: "Hello, my name is Bob"
person1.sayAge() # Will print: "My age is 21"
person1.birthday() # Nothing will be printed, but person1 age value will be incremented
person1.sayAge() # Will print: "My age is 22"
```

# self Paramater

The `self` parameter is a reference to the current instance of the class. It is used to access variables that belong to the object.

It can be called anything you want, but it must be the first parameter passed. It is safe to continue to use `self` for standardisation, and readability for others.