# initFile2.py
# This program checks if the file 'count.txt' exist by returning the number from the file,
# and if it doesn't retuns 0
# Author: Anja Antolkovic

# putting the file into an object
filename = "count.txt" 

# defining the function
def readNumber():
    try: # testing the block of code
        with open(filename) as f:
            number = int(f.read())
            return number
    except IOError: # defining the exception block for input/output error
        return 0

# testing the function
num = readNumber() 
print (num)