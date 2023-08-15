# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 20:04:00 2018

@author: becneljj
"""

# get the numerical grade from the user
grade = float(input("Enter the students numberical grade: "))

letter_grade = "A"   # variable to use the letter grade
"""we assign the letter grade based on the standard
# 10 point scale
90-100 A
80 < 90 B
70 < 80 C
60 < 70 D
0 < 60 F
"""
if (grade >= 90):
    letter_grade = "A"
elif (grade < 90) and (grade >= 80):
    letter_grade = "B"
elif (grade < 80) and (grade >= 70):
    letter_grade = "C"
elif (grade < 70) and (grade >= 60):
    letter_grade = "D"
else:
    letter_grade = "F"

# let the user know the correct letter grade    
print("You earned an ", letter_grade)