# floor.py
# This program takes in a float and outputs an integer rounded down
# Author: Anja Antolkovic

# importing the math module
import math

# place the number
number = float(input("Enter a float number: "))

# rounding down
flooredNumber = math.floor(number)

# printing out
print("{} floored is {}".format(number,flooredNumber))

