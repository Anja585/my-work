# readDict.py
# This program read in the dictionary object from the file 
# Author: Anja Antolkovic

# importing the module
import json 

# putting the file into an object
filename="testdict.json" 

# defining a function
def readDict(): 
    with open(filename) as f: # open the file for reading in text mode
        return json.load(f) # return the converted file (from JSON to Python)
        
# test the function
somedict = readDict()
print(somedict)