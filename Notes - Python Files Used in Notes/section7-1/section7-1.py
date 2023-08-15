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
def avg_cost(n, failure_rate=0.003):
    """ Here we define the function we want to work with.
        Inputs: n a positive for the number of diodes in the test group
        Output: the long run average cost (or expected cost) of testing 
        of groups of size n
    """
    return 4/n - 5*(1-failure_rate)**n+6


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
    Y = avg_cost(X) # the y-values are computed using the function

    plt.plot(X, Y, color="blue", linewidth=2.5, linestyle="-")
    plt.xlabel('n (group size)')
    plt.ylabel('average cost (cents)')



#-----------------------------------------------------------------
def plot_minimum(location):
    """ This module annotates the plot with the local minimum.
        Input: the input is the location of the local minimum
        Ouput: while there is nothing returned, the current mathlibplot
            will be annotated with the point with x value given
            by the location
    """
    # we use the function and the given location to find
    # the (x,y) value for the point
    x = location
    y = avg_cost(location)
    point = (x, y)
    
    # add the point to the plot
    plt.plot([x], [y], color='green', marker='o', markersize=12)
    
    # we offset the location slightly to make the text more readable
    text_location = (x, y+0.5)    
    plt.annotate('(%s, %s)' % point, xy=text_location)
    
#----------------------------------------------------------
def sensitivity_failure_rate(default_failure_rate, default_solution):
    # make a table for the c and the critical value
    print("failure rate \t group size  \t  average cost")
    rates = np.linspace(0.001, 0.008,8, endpoint=True)
    solution_list = [ ]
    cost_list= [ ]
    for r in rates:
        solution = opt.minimize_scalar(avg_cost, bounds=(1,30), args=r, method='bounded')
        solution_list.append(solution.x)
        cost_list.append(avg_cost(solution.x,r))
        print(r, " \t ", solution.x, "\t", cost_list[-1])
    
    # approximate the derivative
    h = 0.00001
    solution1 = opt.minimize_scalar(avg_cost, bounds=(1,30), args=default_failure_rate+h, method='bounded')
    solution2 = opt.minimize_scalar(avg_cost, bounds=(1,30), args=default_failure_rate-h, method='bounded')
    dndq = (solution1.x-solution2.x)/(2*h)
    
    print("\nThe value of S(n,q) is", dndq*default_failure_rate/default_solution)
    
    # plot n vs q
    plt.figure(2)
    plt.plot(rates, solution_list, color="blue", linewidth=2.5, linestyle="-")
    plt.xlabel('q (failure rate)')
    plt.ylabel('n (group size)')
    
    dAdq = (avg_cost(solution1.x, default_failure_rate+h) - avg_cost(solution2.x, default_failure_rate-h))/(2*h)
    print("\nThe value of S(A,q) is", dAdq*default_failure_rate/avg_cost(default_solution))
    
    
    # plot A vs q
    plt.figure(3)
    plt.plot(rates, cost_list, color="green", linewidth=2.5, linestyle="-")
    plt.xlabel('q (failure rate)')
    plt.ylabel('A (avg cost)')
    
#============================START===========================
plot_function(1,30) #  we plot the function 

# next we find the critical value of the function in order to locate the abs min
solution = opt.minimize_scalar(avg_cost, bounds=(1,30), args=0.003, method='bounded')
 # return the solution
print("The critical value found using minimize_scalar", solution.x)
print("The minimum is approximately", avg_cost(solution.x))

# plot the minimum
plot_minimum(solution.x) # add the minimum to the graph
plt.show() # show the graph

sensitivity_failure_rate(0.003,solution.x)