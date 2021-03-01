# guess3.py
# This program generates a random number between 0 and 100 to guess
# Author: Anja Antolkovic

# importing random module 
import random

randomNumber = int(input("Please guess the number: ")) # place the number here
while randomNumber != random.randint(0,100): # checking the condition and generating random number 
    randomNumber = int(input("Please guess again: ")) # change the condition variables
