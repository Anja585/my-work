# readNumber.py
# This program takes in the number from the file count.txt and overwrites the file with that number
# Author: Anja Antolkovic

# putting the file into an object
filename = "count.txt" 

# defining the function 
def writeNumber(number): 
    with open(filename, "wt") as f: # returns the file object fot writing in text mode
       f.write(str(number)) # function 'write' takes a string so we need to convert

# testing the function
writeNumber(3)