# -*- coding: utf-8 -*-
"""
Created on Sat X2eb  9 11:26:45 2019

@author: becneljj
"""

# -*- coding: utf-8 -*-
"""
Created on X2ri X2eb  8 21:58:48 2019

@author: becneljj
"""

import numpy as np
import sympy as sym
import matplotlib.pyplot as plt


#-------------------------X1 and X2 prime functions-------------------------
def f1(x1,x2):
    return -x1**3-4*x1-x2

def f2(x1,x2, C=1.0/3.0):
    return x1/C

#------------------------------------------

def phase_portrait():
    """This function plots the phase portrait for the dynamical system
    along with the vector field for some initial guesses.
    """
    
    # points to plot 
    X1 = np.linspace(-3,3,200)
    X2 = np.linspace(-3,3,200)
    X1,X2 = np.meshgrid(X1,X2)
    # change in variables at the given points
    dX1 = f1(X1,X2)
    dX2 = f2(X1,X2)
    
    # magnitude of change in variables as a vector
    magnitude= np.sqrt(dX1**2+dX2**2)    
    
    
    # create a figure
    fig = plt.figure()
    axes = fig.gca() # get current axes
    
    # Controlling the initial points of the phase lines
    x1 = [1, -1, -1, 1, 1, -1]
    x2 = [1, 2,  -1 , -2, 0, 0]
    
    #  .T transposes the array to get it into the correct format
    initial_points = np.array([x1,x2 ]).T
    
    # create phase lines at the given initial points
    strm = axes.streamplot(X1, X2, dX1, dX2, density=3, color=magnitude, linewidth=4,
                         cmap=plt.cm.autumn, start_points=initial_points)
    fig.colorbar(strm.lines)
    
    
    # plot starting points as blue dots
    for x,y in zip(x1,x2):
       plt.plot([x1], [x2], 'o', color='blue')
       
     # make a smaller mesh for the vector field
    X1, X2 = np.mgrid[-3:3:10j, -3:3:10j]
    dX1 = f1(X1,X2)
    dX2 = f2(X1,X2)
    
    # plot the vector field
    plt.quiver(X1,X2,dX1,dX2, units="width")
    
    # label the plot
    plt.xlabel("x1 (current)")
    plt.ylabel("x2 (voltage)")
    plt.title("Phase Portrait")
    
    plt.show()

#--------------------------------------------------------------------
    
def vector_field():
    """ This function plots the vector field and contours where the 
    functions f1 and f2 governing the dynamics of the system are 0."""
    
    # label the axes
    plt.xlabel("X1")
    plt.ylabel("X2")
    plt.title("Vector Field")
    
    
    # make a smaller mesh for the vector field
    X1, X2 = np.mgrid[-2:2:10j, -8:8:10j]
    dX1 = f1(X1,X2)
    dX2 = f2(X1,X2)
    
    # plot the vector field
    plt.quiver(X1,X2,dX1,dX2, units="width")
    
     
    # use a dense mesh for the plots
    X1 = np.arange(-2, 2, 0.1)
    X2 = np.arange(-8, 8, 0.1)
    X1, X2 = np.meshgrid(X1,X2)
    
    # plot where the functions are 0
    plt.contour(X1,X2, f1(X1,X2), [0], colors='blue')
    plt.contour(X1,X2, f2(X1,X2), [0], colors='red')
           
    plt.show()
    
    
#-----------------------------------------
def eigen_analysis():    
    """Find the eigenvalues and corresponding eigenvectors for hte system."""
    J = sym.Matrix([[-4,-1], [3,0]])
    print("The eigenvalues and eigenvectors for the system are given by: \n", J.eigenvects())

    
#-----------------------------------------------
    
def sensitivity_analysis_C():
    # find the eigenvalues and eigenvectors 
    C = sym.symbols("C")
    J = sym.Matrix([[-4,-1], [1/C,0]])
    print("The eigenvalues and eigenvectors for the system are given by: \n", J.eigenvects())

 #--------------------------------------------
def robustness():
    # here we find the eigenvalues for the system to test robustness
    R = sym.symbols("R")
    J = sym.Matrix([[-R,-1], [3,0]])
    print("\nThe  eigenvalues for the system are given by: \n", J.eigenvals())


#======================START=================================


vector_field() # plot the vector field for the system
eigen_analysis() # find the eigenvlaues and vectors for the system
phase_portrait() # plot the phase portrait for the system

sensitivity_analysis_C() # perform sensitivity analysis for C

robustness() # perform an analysis of robustness

