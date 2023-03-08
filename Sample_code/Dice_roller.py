# imports operating system library from pythons core libraries
import os
# imports random library from pythons core libraries
import random

# Roll a 6 sided dice
min_value = 1
max_value = 6

print("roling dice")
dice1 = random.randint(min_value, max_value)
print(f"Value is: {dice1}")

print("roling dice")
dice2 = random.randint(min_value, max_value)
print(f"Value is: {dice2}")

print("roling dice")
dice3 = random.randint(min_value, max_value)
print(f"Value is: {dice3}")

totalSum = dice1 + dice2 + dice3
print(totalSum)