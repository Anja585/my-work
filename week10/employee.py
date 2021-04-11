# employee.py
# This program definied a class Employee and is testing the code
# Author: Anja Antolkovic

# importing module
import timesheetentry as tm
import datetime as dt

# defining a class
class Employee: 
    timesheets = [] 
    
    def __init__(self, first, last): 
        self.first = first 
        self.last = last

    def __str__(self): 
        return self.first + ' ' + self.last

    def logminutes(self, project, minutes):
        now = dt.datetime.now
        timesheetentry = tm.Timesheetentry(project, now, minutes)
        self.timesheets.append(timesheetentry)

    def gettotaltime(self): 
        total_minutes = 0 
        for ts in self.timesheets:
            total_minutes += ts.duration
        return total_minutes

# testing the code
if __name__ == "__main__": 
    test = Employee("some", "one")
    assert ("some one" == str(test))
    test.logminutes('p1', 30)
    test.logminutes('p1', 60) 
    mins = test.gettotaltime()
    print (mins) 
    assert( mins == 90)
    print ("all good") 

