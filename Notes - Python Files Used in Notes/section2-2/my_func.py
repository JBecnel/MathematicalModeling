# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 22:09:11 2019

@author: becneljj
"""

def avg(X):
    """This function finds the average of a list, tuple, or set of
    floating point numbers.
    Input: a nonempty list of floating point numbers
    Output a float representing the average of the numbers in the list
    """
    sum = 0
    for x in X:
        sum = sum + x
    
    return sum/len(X)