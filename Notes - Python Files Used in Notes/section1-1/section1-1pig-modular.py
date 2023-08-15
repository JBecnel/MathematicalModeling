# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 08:39:02 2018

@author: becneljj
"""

import  sympy as sym  # used for symbolic manipulation of mathematical expressions
import matplotlib.pyplot as plt # used to make fancy plots
import numpy as np # numerical calculations

#-----------------------------------------------------------------------------
def f(val):
    """ Here we define the function we want to work with.
        Inputs: a real number (float) for the input value to the function
        Output: the value (float) of the function at the given input
    """
    return (0.65-0.01*val)*(200+5*val)-0.45*val

#----------------------------------------------------------------------------
def fprime(val):
    """ This module symbolically takes the derivative of the function f and finds
        the value of the derivative at the given input.
        Input: a real number (float) for the the input value to the function
        Output: the value of the derivative at the given value.
    """
    x = sym.symbols('x') # define the symbol x
    fp = sym.diff(f(x),x)    # take the derivative symbolically
    return fp.subs(x,val) # substitute the value in the expression for the derivative
    

#---------------------------------------------------------
def plot_function(a,b):
    """ This module plots the function f on the interval [a,b].
        Input: two floating point numbers representing the beginning and end
              of the interval
        Output: there is no return value, but a matlib plot is configured with axes
        crossing at the origin
    """
    plt.figure(1,figsize=(8,5)) # we create one figure 

    # the following creates an array of X and Y values
    # the x values start at a and go to b
    X = np.linspace(a, b, 50,endpoint=True)
    Y = f(X) # the y-values are computed using the function

    plt.plot(X, Y, color="blue", linewidth=2.5, linestyle="-")
    plt.xlabel('times (days)')
    plt.ylabel('profit in $')


#------------------------------------------------------------
def find_critical_value(f):
    """This method finds a critical value for the given function f
    by solving a symbolic equation of the derivate. It returns
    the first critical value it finds."""
    
    x = sym.symbols('x') #sympy declare x as a symbol
    fprime_expr =sym.diff(f(x),x) # take the derivative 
    solution_list = sym.solve(fprime_expr, x) # solve the equation
    return solution_list[0] # get the first (and only) solution from the list
  
#-----------------------------------------------------------------
def plot_maximum(location):
    """ This module annotates the plot with the local maximum.
        Input: the input is the location of the local maximum
        Output: while there is nothing returned, the current mathlibplot
            will be annotated with the point with x value given
            by the location
    """
    # we use the function and the given location to find
    # the (x,y) value for the point
    x = location
    y = f(location)
    point = (x, y)
    
    # add the point to the plot
    plt.plot([x], [y], color='green', marker='o', markersize=12)
    
    # we offset the location slightly to make the text more readable
    text_location = (x-0.5, y-0.5)    
    plt.annotate('(%s, %s)' % point, xy=text_location)
    

#============================START===========================

plot_function(0,20) # first we plot the function 

# next we find the critical value of the function in order to locate the abs max
root = find_critical_value(f)  

plot_maximum(root) # add the maximum to the graph
plt.show() # show the graph