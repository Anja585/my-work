# convert.py
# This program takes in a float amount of dollars, and returns that absolute amount in cent
# Author: Anja Antolkovic

# place the amount of dollars here
dollars = float(input("Please enter an amount: "))

# calculating dollars to cents, converting to an absolute value and an integer (no decimal places)
cents = int(abs(dollars*100))

# printing out
print ("That amount in cent is {}".format(cents))

