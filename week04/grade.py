# grade.py
# This program reads in a students percentage mark and prints out corresponding the grade
# Author: Anja Antolkovic

# place the percentage here
percentage = round(float(input("Enter the percentage: ")))
if (percentage < 40): # condition if under 40%
    print ("Fail")
elif (percentage < 50): # if between 40% and 49%
    print ("Pass")
elif (percentage < 60): # if between 50% and 59%
    print ("Merit 2")
elif (percentage < 70): # if between 60% and 69%
    print ("Merit 1")
else: print ("Distinction") # if over 70%
