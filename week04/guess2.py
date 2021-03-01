# guess2.py
# This program keeps prompting the user to guess a number until the user gets the right on.
# In addition the program tells the user if there guess is too high or too low.
# Author: Anja Antolkovic

# place the number here
number = float(input("Please guess the number: "))
while number != 30: # checking the condition
    if number < 30: # if less then 30
        print ("too low")
    else: print ("too high") # if more that 30
    number = float(input("Please guess again: ")) # changing the condition
print("Well done! Yes the number was 30")


