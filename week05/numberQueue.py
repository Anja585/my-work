# numberQueue.py
# This program puts 10 random numbers into a queue, 
# and then takes one number at the time and prints it together with them the remaining numbers in the queue
# Author: Anja Antolkovic

import random # importing random module for generating random number

numbers = [] # creating empty list
for i in range(0,10):
    randomNumber = random.randint(0, 100) # generating random numbers from 0 to 100
    numbers.append(randomNumber) # adding them to the empty list
print("queue is {}".format(numbers))

while len(numbers) > 0: # looping over the list until there are still elements in it 
    print("current Number is {} and the queue is {}".format(numbers[0], numbers[1:])) # printing out first element and rest of the element in the list 
    numbers.pop(0) # removing first element form the list
print("the queue is now empty")

 

