# Variables

Python has no command for declaring variables.
By assigning a value to variable you create it.

```python
x = 5
y = "Test string"
```

# Types

Variables do not need to be declared with a type. 
The type is infered when you assign a value to a variable.
It is possible to change the type even after it has been set.

```python
x = 5               # x is an int type
x = "Test string"   # x is now a str type
```

# Casting

If you want to specify a data type then it is possible via casting.

```python
x = str(3)   # x will be '3'
y = int(3)   # y will be 3
z = float(3) # z will be 3.0
```

# Case Sensitive

Variable names are case sensitive

```python
a = "lowercase variable name"
A = "Uppercase variable name"
```

# Finding the type

You can get the data type of a variable with the type() function

```python
x = 5
y = "Test String"

print(type(x)) # <class 'int'>
print(type(y)) # <class 'str'>
```
