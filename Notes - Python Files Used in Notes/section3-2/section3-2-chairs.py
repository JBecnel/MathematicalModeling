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
    """This method returns the profit for producing
    x wood chairs and y aluminum chairs, where 
    x and y are floatig point numbers greater than 0.
    The function is compute numerically.
    """
    return ( x*(10+31*np.power( x, -0.5)+1.3*np.power( y, -0.2))-18*x
            +y*(5+15*np.power( y, -0.4)+0.8*np.power( x, -0.08))-10*y )


#---------------------------------------------------------
def f_sym(x,y):
    """This method returns the profit for producing
    x wood chairs and y aluminum chairs, where 
    x and y are floatig point numbers greater than 0.
    The function is compute numerically.
    """
    return ( x*(10+31*x**(-0.5)+1.3*y**(-0.2))-18*x
            +y*(5+15*y**(-0.4)+0.8*x**(-0.08))-10*y )


#---------------------------------------------------------
def plot_function_and_contour(f,a,b):
    """ This module plots the function f and the corresponding contour plot
        on the square doamin of [a,b]x[a,b].
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
    axes3d.set_title('Profit')
    axes3d.set_xlabel("x (wood)")
    axes3d.set_ylabel("y (aluminum)")
    
    # Add a color bar which maps values to colors.
    fig3d.colorbar(surface, shrink=0.5, aspect=5)
     
    # make a contour subplot
    fig_contour, axes_contour = plt.subplots()
    contour_plot = axes_contour.contour(X, Y, Z, 15) # contour plot with 10 levels
    axes_contour.clabel(contour_plot, inline=1, fontsize=10) # label the contours
    #label the axes
    axes_contour.set_title('Profit')
    axes_contour.set_xlabel("x (wood)")
    axes_contour.set_ylabel("y (aluminum)")
    plt.show()
    
#---------------------------------------------------------------------------
def steepest_ascent(x0, y0, step_size =0.1, iterations = 100):
    """The function performs the steepest ascent method using the
    step size and for the prescribed number of iterations.
    Inputs: x0, y0 are the intial guess
           step_size is how much of the gradient to follow
           iterations - the # of iterations to perform
    Output: a point [x,y] approximating the location for a local
            maximum of the function
    """
    # symbols for the partial derivative
    x = sym.symbols("x")
    y= sym.symbols("y")
    
    # symbolically take the partial derivatives
    dfdx = sym.diff(f_sym(x,y),x)
    dfdy = sym.diff(f_sym(x,y),y)
    
    # function to compute the gradient <df/dx df/dy>
    gradient = lambda a,b : [dfdx.subs({x:a,y:b}), dfdy.subs({x:a,y:b})]
    point = [x0,y0] # starting guess
    
    # for the prescribed number of iteration
    for k in range(0,iterations):
        # find the gradient at the current point
        grad = gradient(point[0],point[1])
        # move in the direction of the gradient points
        point = [point[0]+step_size*grad[0], point[1]+step_size*grad[1]]
    
    return point # retrun the approximation

#----------------------------START-----------------------------
plot_function_and_contour(f,0.5,10)

x = sym.symbols("x")
y= sym.symbols("y")
print("The partial with respect to x",sym.diff(f_sym(x,y),x))
print("\nThe partial with respect to y",sym.diff(f_sym(x,y),y))
x0,y0, max =gridsearch.grid_search_maximum(f,0.5,11,0.5,11, 0.1, 0.1)
print("\nGrid Search results: x=", x0, " y0=", y0, " max=",max)
x0,y0=steepest_ascent(4.5,6)
print("\nSteepest Ascent results: ", x0,y0, " with max of", f(x0,y0) )

bnds = ((0.5,10),(0.5,10)) # bounds for each variable
guess = [4.5, 6]
f_neg = lambda X : -f(X[0],X[1])
solution = opt.minimize(f_neg, guess, method='Nelder-Mead')
print("\nThe solution from scipy optimze:\n", solution)

