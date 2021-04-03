# salaries4.py
# This program makes a list of same 10 random salaries between 20000 and 80000 plus increased by 5%
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

# NumPy allows arithmetic operations on arrays
salariesNew = randomSalaries * 1.05

print(salariesNew)
