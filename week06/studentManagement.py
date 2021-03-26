# studentManagement.py
# Putting together all previously created programms (from week06) into one program 
# The program allows users to add a new student into a students' record (name, modules and grades) and view students' modules and grades 
# Author: Anja Antolkovic

# defining a fuction that prints out the command menu and returns the user's input
def commandMenu():
    print("What would you like to do?\n\t(a) Add new student\n\t(v) View students\n\t(q) Quit")
    command = input("Type one letter (a/v/q):")
    return command

# generating an empty list to add students dictionary records to
students = []

# defining a function that generates a student dictionary record from user's input and append it to an empty list 
def doAdd():
    currentStudent = {}
    currentStudent["name"] = input("enter name :")
    currentStudent ["modules"] = readModules()
    students.append(currentStudent)

# defining the function to print out all out all the student names
def doView():
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"])

# defining the function to print out all modules and grades 
def displayModules(modules):
    print("\tName \tGrade")
    for module in modules:
        print("\t{} \t{}".format(module["name"], module["grade"]))

# defining the function 
def readModules():
    modules = [] # generating empty list
    moduleName = input("\tenter the first Module name (blank to quit) :") # place the module name here
    while moduleName != "": # checking the condition 
        module = {} # creating dictionary for module's name and grades
        module["name"] = moduleName
        module["grade"] = str(input("\t\tenter grade:"))
        modules.append(module) # append the module to an empty list
        moduleName = input("\tenter next module name (blank to quit) :") # change the condition variable
    return modules # return module list

# main program
choice = commandMenu() 
while choice != "q": # checking the condition
    if choice == "a": 
        doAdd()
    elif choice == "v": 
        doView()
    choice = commandMenu() # call the function if the input is condition is true

