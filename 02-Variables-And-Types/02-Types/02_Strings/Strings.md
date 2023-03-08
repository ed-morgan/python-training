# Strings

Strings are a contiguous set of characters represented by quotes.
You can use either single or double quotes.

```python
doubleQuoteStr = "Double Quotes Test String"
singleQuotesStr = "Single Quotes Test String"
```

## Subsets

It is possible to get a subset of a string by using the slice operator.
The first character is index 0

```python
str = "Hello world"

print(str) # Print the complete string - Hello World
print(str[0]) # Prints the first character of the string - H
print(str[2:5]) # Prints string from character 2 to 5 - llo
print(str[3:]) # Prints string from character 3 to end - llo world
```

# Concatination

You can add a string onto the end of the end of another string.

```python
str = "Hello world"

str + "TEST"

print(str) # Hello worldTEST
```
