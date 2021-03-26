# commands.py
# This program prints out a menu of commands we can perform, ie add, view and quit
# The program then returns what the user chose
# Author: Anja Antolkovic

# defining a fuction that prints out the command menu and return the user's input
def commandMenu():
    print("What would you like to do?\n\t(a) Add new student\n\t(v) View students\n\t(q) Quit")
    command = input("Type one letter (a/v/q):")
    return command
    
# testing the function
choice = commandMenu()
print("you chose {}".format(choice))








    