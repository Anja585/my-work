# plotFunction.py
# This program plots the function y = x**
# Author: Anja Antolkovic

# importing the modules
import matplotlib.pyplot as plt
import numpy as np

# defining the variables
xpoints = np.array(range(1, 101))
ypoints = xpoints * xpoints

# plotting the function
plt.plot(xpoints, ypoints)
plt.show()