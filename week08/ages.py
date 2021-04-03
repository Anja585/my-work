# ages.py
# This program makes a list or 10 random age values 21 - 65  and radom salaries 20000 - 80000 
# that are the same each time the program is run, and makes a scatter plot out of them
# Author: Anja Antolkovic

# import the module
import numpy as np
import matplotlib.pyplot as plt

# defining the variables 
minSalary = 20000
maxSalary = 80000
numSalaries = 10
minAge = 21
maxAge = 65
numAgeValues = 10

# radnom number generator will produce the same numbers over again
np.random.seed(1)

# generating random array
randomSalaries = np.random.randint(minSalary, maxSalary, numSalaries)
randomAgeValues = np.random.randint(minAge, maxAge, numAgeValues)

# scattering the functions
plt.scatter(randomAgeValues, randomSalaries)

plt.show()

