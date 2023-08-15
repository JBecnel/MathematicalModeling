# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 22:37:42 2019

@author: becneljj
"""

# dictionary with names as keys and grades as values
grades = { "Joe": 56, "Hanna":87, "Walt":64, "Ali":93}

# find a value using a key
print("Joe's grade is", grades["Joe"])
print("Joe's grade is",grades.get("Joe"))

# add a student
grades["Bob"] = 78
print("\nBob should be in our dictionary",grades)

# remove a student
del grades["Joe"]
print("\nJoe is no longer in the dictionary", grades)

# ask if a student is in the dictionary
print("\nCheck for Joe:", "Joe" in grades)
print("Check for Bob:", "Bob" in grades)

# all the current students
print("\nAll the current students:", grades.keys())
# all the grades
print("All the current grades", grades.values())
# all the entries
print("All the entries in grades", grades.items())

# find the highest grade
max = 0
for student in grades.keys():
    if (grades[student] > max):
        max = grades[student]
print("\nThe max grade is", max)
# note: we could have just sorted the list

# find the lowest grade
min = 100
student_name = ""
for student, grade in grades.items():
    if (grade < min):
        min = grade
        student_name = student
# note: we could have just sorted the list
        
print("\nThe student with the lowest grade is", student_name, " with a grade of",min)