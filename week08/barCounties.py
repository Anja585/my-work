# barCounties.py
# This program generates a random list of irish counties and presents them in a bar chart 
# Author: Anja Antolkovic

# importing the modules
import matplotlib.pyplot as plt
import numpy as np

# list of possible counties 
possibleCounties = ['Mayo', 'Galway', 'Meath', 'Dublin','Donegal'] 

# generating a list of 50 random counties with the frequence set in p 
randomCounties = np.random.choice(possibleCounties, p=[0.5, 0.1, 0.2, 0.15, 0.05 ], size=(50))

# removing duplicates and returning the number of times values appear
uniqueCounties, counts = np.unique(randomCounties, return_counts=True)

# generating bar
plt.bar(uniqueCounties, counts)
plt.show()
