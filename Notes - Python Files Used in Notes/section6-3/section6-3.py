# -*- coding: utf-8 -*-
"""
Created on X2ri X2eb  8 21:58:48 2019

@author: becneljj
"""

import numpy as np   #numerical calculations
import sympy as sym  # symbolic solver
import scipy.integrate as de # differential equation solver
import matplotlib.pyplot as plt # fancy plotting


#-------------------------X1 and X2 prime functions-------------------------
def f1(x1,x2):
    return -x1**3+x1-x2

def f2(x1,x2, C=1.0):
    return x1/C

def F(x, t, C=1.0):
    return [f1(x[0],x[1]), f2(x[0],x[1],C)]
    
#--------------------------------------------------------
def approximate_solution(initial_state=[-1,-1.5], C=1.0):
    """This function approximates the folustion to the differntial equation
    and plot the graph."""
    
    # find the ode solution approximation
    t = np.arange(0, 20, 0.1)
    solution = de.odeint(F, initial_state, t, args=(C,))
    x1 = solution[:,0]
    x2 = solution[:,1]
    
    # plot the approximation
    plt.figure()
    plt.xlabel("x1 (current)")
    plt.ylabel("x2 (voltage)")
    plt.title("C = " + str(C))
    plt.plot(x1, x2, 'b-')

    # put a marker on the starting point
    point = tuple(initial_state)
    x = point[0]
    y = point[1]
    # add the point to the plot
    plt.plot([x], [y], color='green', marker='o', markersize=12)
    
    # we offset the location slightly to make the text more readable
    text_location = (x, y+0.2)    
    plt.annotate('(%s, %s)' % point, xy=text_location)
    plt.show()
    
    # plot each variable versus time
    plt.figure()
    plt.plot(t,x1, linestyle ="-", color="blue")
    plt.plot(t,x2, linestyle ="-", color="green")
    
    plt.ylabel("x1, x2")
    plt.xlabel("time")
    plt.title("Values vs. Time x1 (Green), x2 (Blue)")
    plt.show()


#--------------------------------------------------------    
def phase_portrait(C=1.0):
    """This function plots the phase portrait for the dynamical system
    along with the vector field for some initial guesses.
    """
    
    # points to plot 
    X1 = np.linspace(-2,2,100)
    X2 = np.linspace(-2,2,200)
    X1,X2 = np.meshgrid(X1,X2)
    # change in variables at the given points
    dX1 = f1(X1,X2) 
    dX2 = f2(X1,X2, C)
    
    # magnitude of change in variables as a vector
    magnitude= np.sqrt(dX1**2+dX2**2)    
    
    # create a figure
    fig = plt.figure(3)
    axes = fig.gca() # get current axes
    
    # Controlling the initial points of the phase lines
    x1 = [0.5, -0.5, 0.5, -0.5, -1, 1.5, -1, 1.5]
    x2 = [0.5, 0.5, -0.5, -0.5, 1.5, -1, -1.5, 1]
    
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
    X1, X2 = np.mgrid[-2:2:10j, -2:2:10j]
    dX1 = f1(X1,X2)
    dX2 = f2(X1,X2, C)
    # magnitude of change in variables as a vector
    magnitude= np.sqrt(dX1**2+dX2**2)    
    
    # plot the vector field
    plt.quiver(X1,X2,dX1/magnitude,dX2/magnitude,units='xy', scale=4)
    
    # label the plot
    plt.xlabel("x1 (current)")
    plt.ylabel("x2 (voltage)")
    plt.title("Phase Portrait")
    
    plt.show()
    
#-----------------------------------------------
    
def sensitivity_analysis_C():
    # find the eigenvalues and eigenvectors 
    C = sym.symbols("C")
    J = sym.Matrix([[1,-1], [1/C,0]])
    print("The eigenvalues and eigenvectors for the system are given by: \n", J.eigenvects())

    for c in [0.5,  1.0, 2.0]:
        for init in [[-1,-1.5], [0.1,0.3]]:
            approximate_solution(init, c)

#======================START=================================

for init in [[-1,-1.5], [0.1,0.3]]:
    approximate_solution(init)

phase_portrait()

sensitivity_analysis_C() # perform sensitivity analysis for C




