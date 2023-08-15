# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 22:11:37 2019

@author: becneljj
"""

import math # need to perform root

def geom_avg(X):
    """This function finds the geometric average of a list, tuple, or set of
    floating point numbers.
    Input: a nonempty list of floating point numbers
    Output a float rep
    """
    product = 1
    for x in X:
        product = product * x
    
    return math.pow(product, 1/len(X))