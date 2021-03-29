# testdict.py
# This program stores a simple dictionary to a file as JSON
# Author: Anja Antolkovic

# importing the module
import json 

# putting the file into an object
filename="testdict.json"

# defining a dictionary object
sample= dict(name='fred', age=31, grades=[1,34,55])

# defining a function 
def writeDict(obj): 
    with open(filename, 'wt') as f: # return/create the file object for writing in text mode
        json.dump(obj,f) # convert the dictionary to json and dump to the file 
        
#test the function
writeDict(sample)