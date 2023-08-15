# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 21:58:48 2019

@author: becneljj
"""

import numpy as np
import matplotlib.pyplot as plt

def R_prime(x,y):
    return 2*x - x*y

def F_prime(x,y):
    return -5*y + y*x

def phase_portrait():
    # points to plot for rabbits and foxes
    R = np.linspace(0,15,200)
    F = np.linspace(0,10,200)
    R,F = np.meshgrid(R,F)
    # change of rabbit and fox populations at the given points
    dR = R_prime(R,F)
    dF = F_prime(R,F)
    
    # magnitude of change in population as a vector
    magnitude= np.sqrt(dR**2+dF**2)    
    
    
    # create a figure
    fig = plt.figure()
    axes = fig.gca() # get current axes
    
    # Controlling the initial points of the phase lines
    x0 = [5, 5, 5, 4, 2, 5]
    y0 = [5, 2,  9, 8, 2, 3]
    # note .T transposes the array to get it into the correct format
    initial_points = np.array([x0,y0 ]).T
    
    # create phase lines at the given initial points
    # color=dR shows rabbits
    # color=dF shows foxes
    # color speed shows both
    # cmap=plt.cm.autumn .rainbox .jet https://matplotlib.org/users/colormaps.html
    strm = axes.streamplot(R, F, dR, dF, color=magnitude, linewidth=2,
                         cmap=plt.cm.autumn, start_points=initial_points)
    fig.colorbar(strm.lines)
    
    # label the axes
    plt.xlabel("R (rabbits)")
    plt.ylabel("F (foxes)")
    plt.title("Rabbits vs. Foxes")
    
    
    # make a smaller mesh for the vector field
    R, F = np.mgrid[0:15:10j, 0:10:10j]
    dR = R_prime(R,F)
    dF = F_prime(R,F)
    
    # plot the vector field
    plt.quiver(R,F,dR,dF, units="width")
    
    # plot the starting points as blue dots   
    for x,y in zip(x0,y0):
        plt.plot([x0], [y0], 'o', color='blue')
            
    
    plt.show()


#=============================================================
phase_portrait()