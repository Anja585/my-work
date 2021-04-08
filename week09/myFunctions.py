# myFunctions.py
# This program takes in the number and returns a list containing a Fibonacci sequence of that many numbers
# The program also does the testing of the code
# Author: Anja Antolkovic

# defining the function
def fibonacci(number):
    a = 0
    b = 1
    fibonacciSequence = [0]
    if number < 0: # condition for negative numbers
        raise ValueError('number must be > 0') # raise a value error
    if number == 0: # condition for zero
        return [] # return empty list
    for i in range(1,number): # condition if positive number 
        fibonacciSequence.append(b) # append b to the list
        a , b = b, a + b # a=b and b=b+a
        i+=1 # change the condition
    return fibonacciSequence # return the list
    

#testing the code
if __name__ == "__main__": # if code is the main variable
    # defining the variables
    return7 = [0,1,1,2,3,5,8] 
    return11 = [0,1,1,2,3,5,8,13,21,34,55] 
    # testing the function for different number values
    assert fibonacci(7) == return7
    assert fibonacci(11) == return11 
    assert fibonacci(0) == []  
    assert fibonacci(1) == [0] 
    print("all good")

# testing the function for negative numbers
try:  
    fibonacci(-1) 
except ValueError: # testing if the function will throw value error 
    pass # do nothing
else: # if there is no value error 
    assert False # raise AssertionError

