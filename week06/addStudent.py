# addStudent.py
# This program allow users to add a new student into a student directory. It does the following: 
  # Reads in the students' names 
  # Creates a list for courses' names and grades 
  # Creates a student record dictionary
  # Adds student record dictionary to a list
# Author: Anja Antolkovic

# generating an empty list to add students dictionary records to
students = []

# defining a function that returns a list of modules
def readModules():
    return[]

# defining a function that generates a student dictionary record from user's input and append it to an empty list 
def doAdd():
    currentStudent = {}
    currentStudent["name"] = input("enter name :")
    currentStudent["modules"] = readModules()
    students.append(currentStudent)

# testing the function
doAdd()
doAdd()
print(students)
    

