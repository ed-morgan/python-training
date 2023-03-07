# Functions

A `function` is a block of code which only runs when you call it.
It is possible to pass data and parameters into a function. Parameters can also be called arguements
A function is able to return data as a result.

Functions are useful for creating a reusable body of code. 

A general rule, if you ever write the same piece of code twice, move it to a function.

## Creating a function

A `function` is defined using the `def` keyword

```python

def my_function():
    print("Hello from a function")
```

## Calling a function

To call a function, you use the function name followed by parathesis:


```python

def my_function():
    print("Hello from a function")

my_function()
```

# Arguments

Information can be passed to a function using arguments. 
Arguments are defined when you define the function. 
Arguments are listed in the paratheses after the function name. You can list as many arguements as you want, you just seperate them with a comma.

In the function below, we will define an arguement called name. Then when you call the function, you must pass in the variable in the paratheses

```python

def my_function(name):
    print("Hello " + name)

my_function("Billy") # Will print: "Hello Billy"
my_function("Bob") # Will print: "Hello Bob"
```

```python

def my_function(name, age):
    print("Hello " + name + ", you are " + age " years old")

my_function("Billy", 20) # Will print: "Hello Billy, you are 20 years old"
my_function("Bob", 21) # Will print: "Hello Bob, you are 21 years old"
```

# Default Arguments

It is possible to define a default value for each argument. That way if you call a function and don't pass in a value, it uses the default.

```python

def my_function(city="London"):
    print("I live in " + city)

my_function() # Will print: "I live in London"
my_function("Manchester") # Will print: "I live in Manchester"
```

# Return Values

It is possible for a function return a value. We use the `return` statement.
This value can be used then be used by variable where the function was originally called.

```python

def my_function(a, b):
    return a + b

sum = my_function(1, 2)
print(sum) # Will print: 3
```

# Argument types

Any type can be passed in as a variable. It will be treated as the data type in the function as it is passed in as.

It is important that if you require an argument to be a certain type to include a check inside the function.


```python

def my_function(city):

    if not isinstance(city, str):
        print "City must be a string"
        return

    print("I live in " + city)

my_function("Manchester") # Will print: "I live in Manchester"
my_function(1) # Will print: "City must be a string" and then exit the function
```