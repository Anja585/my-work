# commands2.py
# This program keeps displaying the menu until the user picks q
# The program then returns what the user chose
# Author: Anja Antolkovic

# defining a fuction that prints out the command menu and returns the user's input
def commandMenu():
    print("What would you like to do?\n\t(a) Add new student\n\t(v) View students\n\t(q) Quit")
    command = input("Type one letter (a/v/q):")
    return command

# defining the function that runs if the used picks a
def doAdd():
    print("in adding")

# defining the function that runs if the used picks v
def doView():
    print("in viewing")

# main program
choice = commandMenu() 
while choice != "q": # checking the condition
    if choice == "a": 
        doAdd()
    elif choice == "v": 
        doView()
    choice = commandMenu() # call the function if the input is condition is true
    
       



