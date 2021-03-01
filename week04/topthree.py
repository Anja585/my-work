# topthree.py
# This program generates 10 random numbers from 0-100 and prints out the top three
# Author: Anja Antolkovic

# importing random module
import random
# creating empty list
randomList = []
for i in range(0,10): # checking the condition
    randomNumber = random.randint(0,100) # generating random number
    randomList.append(randomNumber) # appending the number to the list
print("10 random numbers  {}".format(randomList))
sortedList = sorted(randomList) # sorting the numbers in the list from smallest to largest
print("The top 3 are      {}".format(sortedList[-3:])) # returning the last 3 from the list
