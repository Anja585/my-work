# randomFruit2.py
# This program prints out a random fruit
# Author: Anja Antolkovic

# importing random module
import random 

# tuple of random fruits
fruits = ("Apple", "Banana", "Strawberries", "Blueberries")

# generating random number for items in the tuple, first items has index 0 
index = random.randint(0,len(fruits)-1) 

fruit = fruits[index]

print("A Random Fruit: {}".format(fruit))