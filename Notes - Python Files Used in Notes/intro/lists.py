# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 21:40:52 2018

@author: becneljj
"""

# list can be created with [ ]
my_list = ["Jim", "Dwight", "Phyllis", "Stanley"]

# list items are indexed starting at 0
print(my_list[0])

# you can change a list and have duplicate elements
my_list[1] = "Jim"

# the in keyword can check to see if something is in the list
list_has_dwight ="Dwight" in my_list
print("Is Dwight in the list?", list_has_dwight ) 

# len with give you are length of the list
print(len(my_list))

"""
What will be the output of each of the following?
"""

#print(my_list * 2)

#print(my_list[4])
#print(my_list[-1])