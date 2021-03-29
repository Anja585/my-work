# countRun.py
# This program counts how many times the program has been run
# Author: Anja Antolkovic

# putting the file into an object
filename = "count.txt" 

# defining the function 
def readNumber():
    with open(filename) as f: # returns the file object for reading in text mode
        number = int(f.read()) # read the number from the file
    return number # returns the number from the file 

# defining the function 
def writeNumber(number): 
    with open(filename, "wt") as f: # returns the file object fot writing in text mode
       f.write(str(number)) # function 'write' takes a string so we need to convert    
             
# main program
num = readNumber()
num += 1 
print ("we have run this program {} times".format(num)) 
writeNumber(num)