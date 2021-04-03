# salaries2.py
# This program makes a list of 10 random salaries 20000 - 80000 that are the same each time the program is run
# Author: Anja Antolkovic

# import the module
import numpy as np

# defining the variables 
minSalary = 20000
maxSalary = 80000
numSalaries = 10

# radnom number generator will produce the same numbers over again
np.random.seed(1)

# generating random array
randomSalaries = np.random.randint(minSalary, maxSalary, numSalaries)
print(randomSalaries)
