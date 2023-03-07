# Tuples

Tuples are another compound data type that are similar to lists.
A tuple also contains a number of items seperated by commas.
However unlike lists they are enclosed by ().
Tuples are also immutable. Can be thought of Read-Only Lists

```python
tuple = ("Test", "tuple", "example")
mixedTuple = ["Test", 100, "tuple", 50.5]
```

## Subsets

It is possible to get a subset of a list by using the slice operator.
The first item is index 0

```python
list = ["Test", "tuple", "example", 1, 2, 3]

print(list) # Print the complete tuple - ["Test", "tuple", "example"]
print(list[0]) # Prints the first item of the tuple - ["Test"]
print(str[2:5]) # Prints tuple from items 3 to 5 - ["example", 1, 2]
print(str[3:]) # Prints tuple from item 3 to end - ["example", 1, 2, 3]
```