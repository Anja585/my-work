# week07-files.py
# This are the programs from a lab sheet from week07 and answers to the quiz questions  
# Author: Anja Antolkovic

# a. Look at the program below, assuming that the file test-a.txt does not exist.
#    What will happen when the program runs?
#    Answer: Error message

# the with statement will automatically close the file
# when it is finished with it
with open("test-a.txt") as f:
    data = f.read()
    print(data)
# this is the same as
# f = open ("test1.txt")
# data = f.read()
# print(data)
# f.close()

# b. Look at the program below, Assuming the file test-b.txt does not exist, 
#    what will be outputted to the console when this program is run?
#    Answer: 7
#            13
# c. What will the contents of the file test-b.txt be when this program is run?
#    Answer: another line

# the with statement will automatically close the file
# when it is finished with it
with open("test-b.txt", "w") as f:
    data = f.write("test b\n") # returns the number of chars written
    print(data)

with open("test-b.txt", "w") as f2: # open file again
    data = f2.write("another line\n")
    print(data)

# d. Look at the modified program below, what will the contents of the file be after this program is run.
#    Answer: test d
#            another line

# The with statement will automatically close the file
# when it is finished with it
with open("test-d.txt", "w") as f:
    data = f.write("test d\n") # returns the number of chars written
    print(data)
with open("test-d.txt", "a") as f2: # open file again
    data = f2.write("another line\n")
    print(data)


