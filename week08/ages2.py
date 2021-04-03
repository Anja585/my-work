# ages2.py
# This program makes a list or 10 random age values 21 - 65  and radom salaries 20000 - 80000 
# that are the same each time the program is run, makes a scatter plot out of them,
# and adds a line to this plot that shows y= x** in a different colour
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
xpoints = np.array(range(1, 101))
ypoints = xpoints * xpoints

# radnom number generator will produce the same numbers over again
np.random.seed(1)

# generating random array
randomSalaries = np.random.randint(minSalary, maxSalary, numSalaries)
randomAgeValues = np.random.randint(minAge, maxAge, numAgeValues)

# scattering the functions
plt.scatter(randomAgeValues, randomSalaries)

# plotting the function
plt.plot(xpoints, ypoints, color = 'r')

# showing the plot
plt.show()