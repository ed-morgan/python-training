# Conditionals

Python offers flow control with the conditional statements `if`.
Python does not have switch statements, but it is possible to implement them using dictionaries.

## If

If statements are used for decision-making operations. 
It contains a body of code that only runs when the if statement is true.
If the condition is false you can trigger a second body of code by using a else statement. This is optional however.

```python
testInt = 6

if testInt > 5:
    print("testInt is greater than 5")
else:
    print("testInt is less than 5")

```

## Elif

Elif statements enable us to have multiple conditionals, and you are still able to end with a else statement as previously mentioned to.
It is possible to add as many elif statements as you want. The else is still optional

```python
testInt = 6

if testInt > 5 && testInt < 10:
    print("testInt is greater than 5, but less than 10")
elif testInt => 10:
    print("testInt is greater or equal to 10")
else:
    print("testInt is less than 5")

```

## Nested If

It is possible to nest these If statements inside one another.

```python
testInt = 6

if testInt > 5:
    if testInt > 10:
        print("testInt is greater than 10")
    else:
        print("testInt is greater than 5, but less than 10")
```

## Switch Case

Although its not possible to innately use switch statements, they are multiway branch statements that compare a value, and find a body of code that match that value to execute.

In the pseudocode example below, you provide the switch statement with a value (labeled arguement in this example). If the value is equal to 0, 1 or 2 then it will run the corrisponding body of code. It is possible to add a default to the end, so if it doesn't match any case it runs the default body of code.

```
    switch(argument) {
        case 0:
            print("Case 0")
        case 1:
            print("Case 1")
        case 2:
            print("Case 2")
        default:
            print("default")
    }
```
