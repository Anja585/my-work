# initFile.py
# This program checks if the file 'count.txt' exist and initializes the file by putting 0 into it if it does
# Author: Anja Antolkovic

# importing os module
import os.path 

# putting the file into an object
filename = "count.txt" 

# defining the function  
def writeNumber(number): 
    with open(filename, "wt") as f: # returns the file object for writing in text mode
       f.write(str(number)) # overwrites the number into the file


if not os.path.isfile(filename): # checking that the file does not exist
    print ("File does not exist") 
else: writeNumber(0) # initialize file here if the condition is true


