# div.py
# This program reads in two numbers and divides the first one by the second and give the integer result and the remainder
# Author: Anja Antolkovic

# enter first number
number1 = int(input("Enter first number: "))

# enter second number
number2 = int(input("Enter the number you want to divide by: "))

# performs the division answer being an integer
answer1 = int(number1/number2)

# gives the remainder  
answer2 = number1%number2

# prints the answer
print ("{} divided by {} is {} with a remainder {}" .format(number1, number2, answer1, answer2))