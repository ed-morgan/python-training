# imports operating system library from pythons core libraries
import os
# imports random library from pythons core libraries
import random

def roll_dice():
    min_value = 1
    max_value = 6

    # Ask the user how many dice they want to roll
    number_of_dice = int(input('Number of dice: '))
    
    print(f"Rolling {number_of_dice} dice")

    for i in range(number_of_dice):
        dice = random.randint(min_value, max_value)
        print(f"Value is: {dice}")
    
    return dice

roll_dice()