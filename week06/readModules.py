# readModules.py
# This program keeps reading modules until the user enters a module name of blank
# Author: Anja Antolkovic

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

readModules() 




