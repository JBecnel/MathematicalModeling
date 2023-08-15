# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 08:39:02 2018

@author: becneljj
"""
import sympy as sym  # used for symbolic mainpulation of mathematical expressions
import matplotlib.pyplot as plt # used to make fancy plots
import numpy as np # numerical calculations
import scipy.optimize as opt # optimization methods

#-----------------------------------------------------------------------------
def f(val, c=0.025):
    """ Here we define the function we want to work with.
        Inputs: a real number (float) for the input value to the function
        Output: the value (float) of the function at the given input
    """
    return (0.65-0.01*val)*(200*np.exp(c*val))-0.45*val

def f_sym(val, c=0.025):
    """ Here we define the function we want to work with for symbolic manipulation.
        Inputs: a real number or expression to be substituted for the input
        Output: an expression representing the function at the given input
    """
    return (0.65-0.01*val)*(200*sym.exp(c*val))-0.45*val

    
#---------------------------------------------------------
def plot_function(a,b):
    """ This module plots the function f on the interval [a,b].
        Input: two floating point numbers representing the beginning and end
              of the interval
        Output: there is no return value, but a matlib plot is consigured with axes
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
def negative_f(val, c=0.025):
    # This simply negative the original function so we can maximize instead
    # of minizime.
    return -1*f(val, c)

def find_critical_value(f, c=0.025):
    """This method finds a critical value for the given function f
    by solving a symbolic equation of the derivate. It returns
    the first critical value it finds."""
    
    solution = opt.minimize_scalar(negative_f, args=c)
    return solution.x # return the solution

#-----------------------------------------------------------------
def plot_maximum(location):
    """ This module annotates the plot with the local maximum.
        Input: the input is the location of the local maximum
        Ouput: while there is nothing returned, the current mathlibplot
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
    
#----------------------------------------------------------
def sensitivity_c(default_c, x_solution):
    # make a table for the c and the critical value
    print("c \t critical value")
    C = np.linspace(0.022, 0.028,7, endpoint=True)
    root_list = [ ]
    for c in C:
        root = find_critical_value(f, c=c)
        root_list.append(root)
        print(c, " \t ", root)
    
    # approximate the derivative
    h = 0.0001
    root1 = find_critical_value(f, c=default_c+h)
    root2 = find_critical_value(f, c=default_c-h)
    dxdc = (root1-root2)/(2*h)
    
    print("\nThe value of S(x,c) is", dxdc*default_c/x_solution)
    
    # plot c vs x
    plt.figure(2)
    plt.plot(C, root_list, color="blue", linewidth=2.5, linestyle="-")
    plt.xlabel('c (exponential parameter)')
    plt.ylabel('x (time in days)')
    
    # plot g vs x
    G = 200*C
    plt.figure(3)
    plt.plot(G, root_list, color="blue", linewidth=2.5, linestyle="-")
    plt.xlabel('g (growth rate lbs/day)')
    plt.ylabel('x (time in days)')
    
    # plot h vs x
    H = [5/c for c in C]
    plt.figure(4)
    plt.plot(H, root_list, color="blue", linewidth=2.5, linestyle="-")
    plt.xlabel('h (initial weight)')
    plt.ylabel('x (time in days)')
    
#============================START===========================
plot_function(0,40) #  we plot the function 

# take the deritivate symbolically
x = sym.symbols('x') # define the symbol x
fp = sym.diff(f_sym(x),x)    # take the derivative symbolically
print("The symbolic derivative is", fp)

# find the value of the derivative using Brent's method
fprime = sym.lambdify(x,fp,"numpy") # make the derivative a numerial function
solution = opt.brentq(fprime,0,50)
print("The critical point using Brent's method", solution)

# next we find the critical value of the function in order to locate the abs max
root = find_critical_value(f)  
print("The critical value found using minimize_scalar", root)
print("The maximum is approximately", f(root))

# plot the maximum
plot_maximum(root) # add the maximum to the graph
plt.show() # show the graph

sensitivity_c(0.025,root)