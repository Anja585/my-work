# studentRecords.py
# This program stores a student's name and a list of courses and grades,
# the program then prints out data. The number of course could also change
# Author: Anja Antolkovic

# creating a dictionary for student name and list of student coursed (list because new courses can be added)
studentRecord = {
    "firstName": "Mary",
    "courses":[{
        "courseName" : "Programming",
        "grade" : "45"
        },{
           "courseName" : "History",
            "grade" : "99"
        }]
}

print("Student: {}".format(studentRecord["firstName"]))
for course in studentRecord["courses"]: # looping through list of dictionaries within a dictionary
    print("\t{} :\t{}".format(course["courseName"], course["grade"])) # returning keys and values from the list of dictinaries

