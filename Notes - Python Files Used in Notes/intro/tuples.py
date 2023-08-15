# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 22:11:19 2018

@author: becneljj
"""

# tuple can be created with ( )
my_tuple = ("Jim", "Dwight", "Phyllis", "Stanley")

# tuple items are indexed starting at 0
print(my_tuple[3])

# you can NOT change a tuple or add to it...the following produces an error
#my_tuple[1] = "Jim"
print(my_tuple[1])

# the in keyword can check to see if something is in the tuple
tuple_has_dwight ="Dwight" in my_tuple
print("Is Dwight in the tuple?", tuple_has_dwight ) 

# len with give you are length of the tuple
print(len(my_tuple))

"""
What will be the output of each of the following?
"""

#print(my_tuple * 2)

#print(my_tuple[4])
#print(my_tuple[-1])