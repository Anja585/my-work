# average.py
# This program keeps reading numbers until the user enters a 0
# The program then prints out each of the numbers entered and calculates the average of them
# Author: Anja Antolkovic

# importing numpy for a mean function
import numpy

# place the number here
number = int(input("enter number (0 to quit): "))
numbers = [] # creating empty list 
while number != 0: # checking the variable condition
    numbers.append(number) # append the number to the empty list
    number = int(input("enter another(0 to quit): ")) # change condition variables

# use * to unpack the numbers from the list separated each on the new line
print(*numbers, sep='\n')
# use mean function to calculate average value
print("The average is {}".format(numpy.mean(numbers)))

