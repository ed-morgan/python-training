# Dictionary

Dictionary are a kind of hash table type.
They consist of key-value pairs.
Dictionary key can be any types but are usually numbers or string.
Values can be any type.

Dictionaries are enclosed by {}, but values can be accessed and assigned by []

```python
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

secondDict = {'name': "testname", 'age': 30, working: True}
```

## Accessing Values

It is possible to get a subset of a list by using the slice operator.
The first item is index 0

```python
dict = {'name': "testname", 'age': 30, 'working': True}

print(dict['name']) # Print the value for key 'name' - "testname"
print(dict) # Prints complete dictionary - {'name': "testname", 'age': 30, 'working': True}
print(dict.keys()) # Prints all the keys - (['name, 'age', 'working'])
print(dict.values()) # Prints all the values- (['testname, 30, 'True'])
```