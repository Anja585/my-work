# normalise.py
# This program reads in a string, strips any leading or trailing spaces and converts the string to lower case
# Author: Anja Antolkovic

# raw string
x = input ("Please enter a string: ")

# striping leading and trailing spaces
y = x.strip()

# converting to lower case 
z = y.casefold()

# calculating the number of characters in raw and converted string
lenghtOfX = len(x)
lenghtOfY = len(y)

# printing the convered string and comparing the number of characters in raw and converted string
print ("That String normalised is: {}".format(z))
print ("We reduced the input string from {} to {} character".format (lenghtOfX,lenghtOfY))

