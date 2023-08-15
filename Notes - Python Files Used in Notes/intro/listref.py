# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 22:03:07 2018

@author: becneljj
"""

# made up list
my_list = [1,2,3]
# use the copy function to make a copy of the list
copy_list = my_list.copy()
# make another variable referencing the list
ref_list = my_list

ref_list[0]="Dilly"

print("List Copy", copy_list)
print("List Reference", ref_list)
print("My list", my_list)