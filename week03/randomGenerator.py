# randomGenerator.py
# This program prints out a random number from the range that user inputs 
# Author: Anja Antolkovic

import random

number1 = int(input ("Enter first number: ")) # place the first number in the range
number2 = int(input ("Enter last number: ")) # place the last number in the range
randomNumber = random.randint(number1,number2) # generates the random number 

print ("here is the random number: {}" .format(randomNumber)) # prints out the number 