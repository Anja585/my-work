# timesheetentry.py
# This program definied a class Timesheetentry and is testing the code
# Author: Anja Antolkovic

# defining a class
class Timesheetentry:
    def __init__(self, project, start, duration): # defining three attributes
        self.project = project
        self.start = start
        self.duration = duration
    
    def __str__(self): # defining a function that retuns project and the duration
        return self.project +':' + str(self.duration) 

# importing the module        
import datetime as dt

# testing the code
if __name__ == '__main__':
    ts = dt.datetime(2021,4,11,14,35) 
    test = Timesheetentry('test', ts , 60) 
    assert (60 == test)
    print ("all good")