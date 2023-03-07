# Lists

Most versatile of Pythons compound data types.
A list contains a number of items sperated by commas and enclosed by [].
Lists can contain different types of items.

```python
list = ["Test", "list", "example"]
mixedList = ["Test", 100, "list", 50.5]
```

## Subsets

It is possible to get a subset of a list by using the slice operator.
The first item is index 0

```python
list = ["Test", "list", "example", 1, 2, 3]

print(list) # Print the complete list - ["Test", "list", "example"]
print(list[0]) # Prints the first item of the list - ["Test"]
print(str[2:5]) # Prints list from items 3 to 5 - ["example", 1, 2]
print(str[3:]) # Prints list from item 3 to end - ["example", 1, 2, 3]
```

# Concatination

You can add a list onto the end of the end of another list.

```python
list = ["Test", "list", "example", 1, 2, 3]
secondList = ["Second", "list"]

list + secondList

print(list) # ["Test", "list", "example", 1, 2, 3, "Second", "list"]
```

# Append

You can append items to end of list using append() method.

```python
list = ["Test", "list", "example"]

list.append("Append")

print(list) # ["Test", "list", "example", "Append"]
```

# Insert

You can insert an item at a specific index using insert() method.

```python
list = ["Test", "list", "example"]

list.insert(1, "Insert")

print(list) # ["Test", "Insert", "list", "example"]
```

# Remove 

You can remove elements from a list using remove() method. 
If there is multiple of the same item, it will remove the first one it finds.
The method returns `None`

```python
list = ["Test", "list", "example", "Test"]

list.remove("Test")

print(list) # ["list", "example", "Test"]
```
