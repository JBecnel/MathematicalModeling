# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 10:53:12 2018

@author: becneljj
"""


#-------------modules in python
def print_number(x):
    print("Output from print_number x = ", x, " id=", id(x))

x=9
print_number(x)

#------------------------------------------
def print_number_change(x):
    print("Output before change x = ", x, " id=", id(x))
    x = 42
    print("Output after change x = ", x, " id=", id(x))
    

x=9
print_number_change(x)
print("Value of main x: ", x)


#-----------------------------------------------------

def double_list(some_list):
    some_list += some_list
    return some_list

list1 = [1,2,3]
print(double_list(list1))
print(list1)


def double_list_ref(some_list):
    some_list += some_list

list2 = [3,2,1]
double_list_ref(list2)
print(list2)

#---------------global versus local--------------
def example():
    print("global x is ", x)
    y = 27 # local
    print("local y is ", y)
    
x = 24 # global
example()
print("x is still ", x)
#print("y is not defined here", y)

#----------------------------------------------------

def add_up(some_list):
    """This function adds up all the element 
    in a given list and returns the total."""
    total = 0
    for x in some_list:
        total = total + x
    return total

my_list = [ 1,2]
sum=add_up(my_list)
print("The total of the list", my_list, "is", sum)

#-----------------------------------------------------

def append_list(some_list, num=100):
    """This function appends a list 
    with a given number. If no number
    is specified 100 is appended to
    the list."""
    some_list.append(num)



append_list(my_list)
print(my_list)
append_list(my_list, num=30)
print(my_list)


