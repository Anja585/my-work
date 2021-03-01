# guess1.py
# This program keeps prompting the user to guess a number until the user gets the right on
# Author: Anja Antolkovic

# place the number here
number = float(input("Please guess the number: "))
while number != 30: # condition for the correct number
    print("Wrong")
    number = float(input("Please guess again: ")) # changing the condition
print("Well done! Yes the number was 30")
