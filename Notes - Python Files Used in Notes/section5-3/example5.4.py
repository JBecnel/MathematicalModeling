# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 08:53:39 2019

@author: becneljj
"""

import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

#-------------------------------------------------------
def example_complex():
    # here we perform example 5.4 from the book
    J = sym.Matrix([[1,-1], [1,0]])
    print("\nThe eigenvalues and eigenvectors for the system are given by: \n", J.eigenvects())

    # points to plot 
    X1 = np.linspace(-1.5,1.5,100)
    X2 = np.linspace(-1.5,1.5,200)
    X1,X2 = np.meshgrid(X1,X2)
    # change in variables at the given points
    dX1 = X1-X1**3-X2
    dX2 = X1
    
    # magnitude of change in variables as a vector
    magnitude= np.sqrt(dX1**2+dX2**2)    
    
    
    # create a figure
    fig = plt.figure(3)
    axes = fig.gca() # get current axes
    
    # Controlling the initial points of the phase lines
    x1 = [0.5, -0.5, 0.5, -0.5]
    x2 = [0.5, 0.5, -0.5, -0.5]
    
    #  .T transposes the array to get it into the correct format
    initial_points = np.array([x1,x2 ]).T
    
    # create phase lines at the given initial points
    strm = axes.streamplot(X1, X2, dX1, dX2, density=3, color=magnitude, linewidth=2,
                         cmap=plt.cm.autumn, start_points=initial_points)
    fig.colorbar(strm.lines)
    
    
    # plot starting points as blue dots
    for x,y in zip(x1,x2):
       plt.plot([x1], [x2], 'o', color='blue')
       
     # make a smaller mesh for the vector field
    X1, X2 = np.mgrid[-1.5:1.5:10j, -1.5:1.5:10j]
    dX1 = X1-X1**3-X2
    dX2 = X1
    # magnitude of change in variables as a vector
    magnitude= np.sqrt(dX1**2+dX2**2)    
    
    # plot the vector field
    plt.quiver(X1,X2,dX1/magnitude,dX2/magnitude,units='xy', scale=4)
    
    # label the plot
    plt.xlabel("x1 (current)")
    plt.ylabel("x2 (voltage)")
    plt.title("Phase Portrait")
    
    plt.show()
    
    
#===========================START============================
example_complex() # example - complex eigenvalues 5.4 in the book
