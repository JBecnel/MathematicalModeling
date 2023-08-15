# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 23:38:58 2019

@author: becneljj
"""
import sympy as sym # symbolic manipulation
import matplotlib.pyplot as plt # used to make fancy plots
from matplotlib import cm # color mapping
import numpy as np # numerical calculations
#from scipy import optimize # used for root finding
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # 
import scipy.optimize as opt # needed for minimization function

import gridsearch # my grid search algorithm

#---------------------------------------------------------
def f(x,y):
    """This method returns the average response time in minutes for
    a fire station located at (x,y).  The function is compute numerically.
    """
    return 3.2+1.7*(6*np.power( np.sqrt((x-1)**2+(y-5)**2), 0.91)
                   +8*np.power( np.sqrt((x-3)**2+(y-5)**2), 0.91)
                   +8*np.power( np.sqrt((x-5)**2+(y-5)**2), 0.91)
                   +21*np.power( np.sqrt((x-1)**2+(y-3)**2), 0.91)
                   +6*np.power( np.sqrt((x-3)**2+(y-3)**2), 0.91)
                   +3*np.power( np.sqrt((x-5)**2+(y-3)**2), 0.91)
                   +18*np.power( np.sqrt((x-1)**2+(y-1)**2), 0.91)
                   +8*np.power( np.sqrt((x-3)**2+(y-1)**2), 0.91)
                   +6*np.power( np.sqrt((x-5)**2+(y-1)**2), 0.91))/84.0


#---------------------------------------------------------
def f_sym(x,y):
    """This method returns the average response time in minutes for
    a fire station located at (x,y). The function is compute symbolically.
    """
    return 3.2+1.7*(6*sym.sqrt((x-1)**2+(y-5)**2)**0.91
                   +8*sym.sqrt((x-3)**2+(y-5)**2)**0.91
                   +8*sym.sqrt((x-5)**2+(y-5)**2)**0.91
                   +21*sym.sqrt((x-1)**2+(y-3)**2)**0.91
                   +6*sym.sqrt((x-3)**2+(y-3)**2)**0.91
                   +3*sym.sqrt((x-5)**2+(y-3)**2)**0.91
                   +18*sym.sqrt((x-1)**2+(y-1)**2)**0.91
                   +8*sym.sqrt((x-3)**2+(y-1)**2)**0.91
                   +6*sym.sqrt((x-5)**2+(y-1)**2)**0.91)/84.0

#---------------------------------------------------------
def plot_function_and_contour(f,a,b):
    """ This module plots the function f and the corresponding contour plot
        on the square domain of [a,b]x[a,b].
        Input: two floating point numbers representing the beginning and end
              of the square grid on the x and y axs
        Output: there is no return value, but a matlib plot constructed
    """
    # create a 3d figure
    fig3d = plt.figure()
    axes3d =  fig3d.gca(projection='3d')

    # Make the mesh grid
    X = np.arange(a, b, 0.1)
    Y = np.arange(a, b, 0.1)
    X, Y  = np.meshgrid(X, Y)
    Z = f(X,Y)
    
    # Plot the surface.
    surface = axes3d.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

    # label the axes
    axes3d.set_title('Response Time')
    axes3d.set_xlabel("x")
    axes3d.set_ylabel("y")
    
    # Add a color bar which maps values to colors.
    fig3d.colorbar(surface, shrink=0.5, aspect=5)
     
    # make a contour subplot
    fig_contour, axes_contour = plt.subplots()
    contour_plot = axes_contour.contour(X, Y, Z, 10) # contour plot with 10 levels
    axes_contour.clabel(contour_plot, inline=1, fontsize=10) # label the contours
    #label the axes
    axes_contour.set_title('Response Time')
    axes_contour.set_xlabel("x")
    axes_contour.set_ylabel("y")
    
    plt.show()
    
#----------------------------START-----------------------------
plot_function_and_contour(f,0,6)

x = sym.symbols("x")
y= sym.symbols("y")


print("\n\nThe results of grid search on the entire domain are:")
print(gridsearch.grid_search_minimum(f,0,6,0,6))

print("\n\nThe results of grid search on the refined domain are:")
print(gridsearch.grid_search_minimum(f,1.5,2,2.5,3,0.02,0.02))
