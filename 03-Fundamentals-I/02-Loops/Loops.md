# Loops

Python has two looping constructs, the 'for' loop and the 'while' loop.

## For

A 'for' loop is used for iterating over a sequence. Whether that be a list, tuple, dictionary, or string.

With a 'for' loop we can execute a body of code once for each item in the set.

```python
fruits = ["apple", "banana", "cherry"]

for x in fruits:
    print(x)
```

**Note:** In the above example, we define x to denote the item we are currently working with. The output will print "apple", "banana", "cherry" in order, one line at a time.


## Looping through a string

Strings are iterable objects as well. They contain a sequence of letters, and as such you can execute a body of code for each letter.

```python
for x in "banana":
    print(x)
```

**Note:** In the above example, The output will print the individual letters of banana line by line.

## Break statement

The `break` statement can be used to stop the loop before it has looped through all the items.

```python
fruits = ["apple", "banana", "cherry"]

for x in fruits:
    print(x)

    if x == "banana"
        break
```

This will exit the loop when it reaches an item that is "banana". 

## Continue statement

The `continue` statement can be used to skip the current interation of the loop and continue with the next one.

```python
fruits = ["apple", "banana", "cherry"]

for x in fruits:

    if x == "banana"
        continue

    print(x)
```

Here we will print out apple, and cherry as when the item equals banana we skip the loop before we print the value.


## Nested loops

It is possible to have a loop within a loop. The inner loops will be executed one time for each time of the outer loop.

```python
outerList = ["green", "red", "blue"]
innerList = ["apple", "banana", "cherry"]

for x in outerList:
    for y in innerList:
        print(x, y)
```

This will output:

* green apple
* green banana
* green cherry 
* red apple
* red banana
* red cherry 
* blue apple
* blue banana
* blue cherry 


## While

A 'while' loop executes as long as the condition is true.

```python
i = 1

while i < 10:
    print(i)
    i = i + 1
```

The loop will print the value of i, then increment i by 1 until it is equal to 10, then it will no longer be true and the body of code will no longer execute.

## Break

`break` statements function the same as with for loops 

## Continue

`continue` statements function the same as with for loops 
