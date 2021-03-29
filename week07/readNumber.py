# readNumber.py
# This program reads in the number from the file 'count.txt'
# Author: Anja Antolkovic

# putting the file into an object
filename = "count.txt"

# defining the function 
def readNumber():
    with open(filename) as f: # returns the file object for reading in text mode
        number = int(f.read()) # read the number from the file
    return number # returns the number from the file 
    
# testing the function
num = readNumber() 
print (num)
