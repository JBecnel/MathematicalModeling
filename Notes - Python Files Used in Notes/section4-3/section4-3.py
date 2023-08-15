# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 08:31:22 2019

@author: becneljj
"""


import sympy as sym # symbolic manipulation
import matplotlib.pyplot as plt # used to make fancy plots
import numpy as np # numerical calculations

#------------------------------------------------
# functions for the rate of change in x1
def f1(x1, x2,  W =1, C=1):
    return -W*x1-C*x2

# functions for the rate of change in x2
def f2(x1, x2):
    return x1-x2

# same as above, but in vector form using np.arrary
# x - is an np.array (vector) representing the current state
# of the system and mult is the multiplier for how the system
# is changing
def F(x,    W =1, C =1):
    return np.array([f1(x[0],x[1],W,C), f2(x[0],x[1])])

#---------------------------------------------------
def plot_vector_field(  W =1, C =1):
    """ This function plots the vector field for the given discrete time
    dynamical system. The optional parameters k, c, w are parameters for the
    underlying vector field.
    """
    
    plt.figure()
    
    # use a sparse mesh for the vector field
    X = np.linspace(-2, 2, 4, endpoint=True)
    Y = np.linspace(-2, 2, 4, endpoint=True)
    X, Y = np.meshgrid(X,Y)
    
    # plot the vector field
    # we want the vectors to be there actual length; 
    #To plot vectors in the x-y plane, with u and v having the same units as x and y, 
    #use angles='xy', scale_units='xy', scale=1.
    plt.quiver(X,Y,f1(X,Y,W,C),f2(X,Y),angles="xy", scale=1.0, scale_units='xy')
    
    # label the axes and the plot
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.title("Vector Field with W =" +str(W) + " C="+str(C))
    
    plt.show()
    
#------------------------------------------
def create_sequence( start = np.array((3,2)), num_points = 10,W =1, C=1):
   """This is method creates a sequences of points demonstrating how our
   discrete time dynamical system is changing. We begin at the starting 
   position given by start, an numpy array (vector). The system is run for the
   number of times steps given by num_poitns and the mult is a parameter of 
   the system
   
   A list of tuples representing the states we traversed is returned.
   """
   # list of points that will be return 
   point_list = [ tuple(start) ]
   current_point = start # loop variable holding the current state of system
   for k in range(num_points):
       # move to the next point in the system
       current_point = current_point + F(current_point,W,C)
       # add the point to our point list
       point_list.append(tuple(current_point))
    
   return point_list # return the sequence of points (as a list of tuples)

#----------------------------------------------------------------------
    
def scatter_plot(points):
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    #https://matplotlib.org/api/_as_gen/matplotlib.pyplot.scatter.html
    # s is the marker size in points
    # alpha  controls transparency
    plt.scatter(x,y, alpha= 0.5, s =400)
    
    index = 0
    for p in points:
        plt.annotate(str(index), p, size = 15)
        index = index +1 
        
    plt.figure()
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.title("Sequence of Points starting at " + str(points[0]))
    plt.show()

#------------------------------------------------------
def find_equilibrium():
    # symbols used in expressions 
    x1,x2 = sym.symbols("x1,x2")
    W = sym.symbols("W")
    C = sym.symbols("C")
    
    # the equilibrium points
    solutions = sym.solve([f1(x1,x2,W,C), f2(x1,x2)], x1, x2)
    
    # The equilibrium solutions are
    print("The equilibrium solutions are", solutions)
    
#===========================START===============================

find_equilibrium()

for c in [1.5, 1.0, 0.3]:
    for w in [1.5, 1.0, 0.3]:
        plot_vector_field(W=w,C=c)
        points = create_sequence(W=w,C=c)
        scatter_plot(points)

for w in [1.5, 1.0, 0.3]:
    points = create_sequence(W=w,C=0.3, num_points=25)
    print("The last point is ", points[-1])
    scatter_plot(points)
