# Booleans

Booleans represent one of two values: `True` or `False`

```python
trueBoolean = True
falseBoolean = False
```

## Evalue Values and Variables

You can use bool() function to evaluate any value and it will return `True` or `False`. It can be used to evaluate values held by variables as well.

```python
print(bool("Hello")) # returns True
print(bool(15)) # return True

x = "hello
y = 15

print(bool(x)) # returns True
print(bool(y)) # return True
```

Most values are True, if the value has some sort of content.

** Any string is True, except for empty strings
** Any number is True, except for 0
** Any list, tuple, dictionary are True, except if they are empty.