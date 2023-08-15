# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 20:03:59 2019

@author: becneljj
"""

def bisection(f,a,b,tol):
    """This function implements the bisection root finding method.
    Input: f - a continuous function with root between the floating
           point inputs a and b
           tol - tells us the level of accuary we are after
    Output: a floating point number approximating the root
           of the function
    """
    c = (a+b)/2.0 # midpoint
    # continue until we get desired accuary
    while (b-a)/2.0 > tol: 
        if f(c) == 0:
            return c
        elif f(a)*f(c) < 0: # check for one + and one -
            b = c
        else:
            a = c
        c = (a+b)/2.0 #new midpoint
		
    return c # return approximation



#-------------------------------
def f(val):
    return val**2-2*val

print("The root is approximately", bisection(f,1,3, 0.001))

