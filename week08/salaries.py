# salaries.py
# This program makes a list that has 10 random salaries betweem 20000 and 80000
# Author: Anja Antolkovic

# import the module
from numpy import random

# defining the variables 
minSalary = 20000
maxSalary = 80000
numSalaries = 10

# generating random array
randomSalaries = random.randint(minSalary, maxSalary, numSalaries)
print(randomSalaries)




