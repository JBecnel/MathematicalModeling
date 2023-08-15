# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 22:26:47 2018

@author: becneljj
"""

# set can be created with {  }
my_set = {"Jim", "Dwight", "Phyllis", "Stanley"}

# NOT indexed - following gives an error
#print(my_set[3])
#my_set[1] = "Jim"

# the in keyword can check to see if something is in the set
set_has_pam ="Pam" in my_set
print("Is Pam in the set?", set_has_pam ) 

# len with give you are length of the set
print(len(my_set))

"""
What will be the output of each of the following?
"""
another_set= {"Jim", "Pam", "Jim"}
print(another_set)

print(another_set.intersection(my_set))
