# isEven.py
# This program asks the user to enter in a number, and tells if the number is even or odd
# Author: Anja Antolkovic

# place the number here
number = int(input("Enter a number: "))
if number % 2 == 0: # condition for the evenness
    print ("{} is an even number".format(number))
else: # condition if not even
    print ("{} is an odd number".format(number))