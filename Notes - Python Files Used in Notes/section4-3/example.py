# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 08:31:22 2019

@author: becneljj
"""



import matplotlib.pyplot as plt # used to make fancy plots
import numpy as np # numerical calculations

#------------------------------------------------
# functions for the rate of change in x1
def f1(x1, x2, mult = 0.5):
    return -mult*x1

# functions for the rate of change in x2
def f2(x1, x2, mult = 0.5):
    return -mult*x2

# same as above, but in vector form using np.arrary
# x - is an np.array (vector) representing the current state
# of the system and mult is the multiplier for how the system
# is changing
def F(x, mult =0.5):
    return -mult*x

#---------------------------------------------------
def plot_vector_field(mult = 0.5):
    """ This function plots the vector field for the given discrete time
    dynamical system. The optional parameter mult is a parameter for the
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
    plt.quiver(X,Y,f1(X,Y, mult),f2(X,Y,mult),angles="xy", scale=1.0, scale_units='xy')
    
    # label the axes and the plot
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.title("Vector Field with lambda =" +str(mult))
    
    plt.show()
    
#------------------------------------------
def create_sequence(mult = 0.5, start = np.array((4,4)), num_points = 10):
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
       current_point = current_point + F(current_point, mult)
       # add the point to our point list
       point_list.append(tuple(current_point))
    
   return point_list # return the sequence of points (as a list of tuples)

#----------------------------------------------------------------------
    
def scatter_plot(points):
    """This function draws a scatter plot given a set of points."""
    plt.figure()
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
        
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.title("Sequence of Points starting at " + str(points[0]))
    plt.show()
    
#===========================START===============================
    
for a in [0.3, 0.5, 1.0, 1.5, 2.0]:
    plot_vector_field(mult=a)
    
points = create_sequence()
print("The sequence of points for this dynamical system is", points)
scatter_plot(points)


for a in [1.0, 1.8, 2.0, 2.4]:
    scatter_plot(create_sequence(mult=a))
