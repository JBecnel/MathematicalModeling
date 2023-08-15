# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 08:39:02 2018

@author: becneljj
"""

import  sympy as sym  # used for symbolic mainpulation of mathematical expressions
import matplotlib.pyplot as plt # used to make fancy plots
from matplotlib import cm # color mapping
import numpy as np # numerical calculations
#from scipy import optimize # used for root finding
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # 
import scipy.optimize as opt # needed for minimization function
import lagrange # my module with Langrange symbolic solver
#-----------------------------------------------------------------------------
def price19(s,t, a=0.01):
    """Thus function computes the selling price of the 19-inch TV
    given the amount of 19-inch and 21-inch models sold along
    with an optional parameter for price elasticity."""
    return 339-a*s-0.003*t

def price21(s,t):
    """Thus function computes the selling price of the 21-inch TV
    given the amount of 19-inch and 21-inch models """
    return 399-0.004*s-0.01*t

def revenue(s,t, a=0.01):
    """Thus function computes the revenue from selling 
    19-inch and 21-inch TV models sold, s and t, along
    with an optional parameter for price elasticity."""
    return price19(s,t,a)*s + price21(s,t)*t

def cost(s,t):
    """Thus function computes the cost of manufacturing 
    19-inch and 21-inch TV models, quantities s and t."""
    return 400000+195*s+225*t

def profit(s,t,a=0.01):
    """Thus function computes the profit from selling 
    19-inch and 21-inch TV models, quantities s and t, along
    with an optional parameter for price elasticity."""
    return revenue(s,t,a)-cost(s,t)

def f(x1,x2, a=0.01):
    """ Here we define the function we want to work with.
        Inputs: two real numbers (floats) for the input value to the function
        Output: the value (float) of the function at the given input
    """
    return profit(x1,x2,a)
    
def f_list(X, a=0.01):
    """ Here we define the function we want to work with.
        Inputs: a list of variables as inputs
        Output: the value (float) of the function at the given input
    """
    return f(X[0],X[1],a)

def f_negative(X, a=0.01):
    """ Here we define the function we want to work with.
        Inputs: a list of variables as inputs
        Output: the value (float) of the function at the given input
    """
    return -f(X[0],X[1],a)

def constraint(X):
    """ This function is a constraint we have on production of the 19 and 
    21 inch sets, X[0] and X[1]"""
    return X[0]+X[1]-10000


#---------------------------------------------------------
def plot_function_and_contour(a,b):
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
    X1 = np.arange(a, b, 25)
    X2 = np.arange(a, b, 25)
    X1, X2 = np.meshgrid(X1, X2)
    Y = f(X1,X2)
    
    # Plot the surface.
    surface = axes3d.plot_surface(X1, X2, Y, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

    # label the axes
    axes3d.set_title('Profit')
    axes3d.set_xlabel("19 inch")
    axes3d.set_ylabel("21 inch")
    
    # Add a color bar which maps values to colors.
    fig3d.colorbar(surface, shrink=0.5, aspect=5)
     
    # make a contour subplot
    fig_contour, axes_contour = plt.subplots()
    contour_plot = axes_contour.contour(X1, X2, Y, 10) # contour plot with 10 levels
    axes_contour.clabel(contour_plot, inline=1, fontsize=10) # label the contours
    #label the axes
    axes_contour.set_title('Profit')
    axes_contour.set_xlabel("19 inch")
    axes_contour.set_ylabel("21 inch")
    
    axes_contour.contour(X1, X2, Y, levels=[532308])   
    S = np.linspace(0,5000, 200)
    T = np.linspace(8000,8000,200)
    for k in range(0, len(T)):
        if (10000-S[k] <= 8000):
            T[k] = 10000-S[k]
            
    
    axes_contour.fill_between(S,0,T)
    plt.show()
    
    # show the plot
    plt.show()
    

    

#============================START===========================

# find a simplified expression for f
x1 = sym.symbols("x1")
x2 = sym.symbols("x2")
expr_for_f = sym.simplify(f(x1,x2))
print("Here is a simplified expression for f(x1,x2)=", expr_for_f)


#  plot the function profit function on a 0-10000 square grid 
plot_function_and_contour(0,10000)

# algebraically solve using largrange multipliers
solution = lagrange.lagrange_algebraic(f_list,[constraint], var_list=["x1","x2"])
print(solution)
print("The exact solutions are at", solution[0], "yeilding a max of", solution[1], 
      "with lambda values", solution[2])

#----------------numerical calculations---------------------
# constraint over which we are maximizing the function
cons = ({'type': 'eq', # eq for equality; ineq for inequality
         'fun' : constraint}  # constraint of the form =0 or >=0
        )
bnds = ((0,5000),(0,8000)) # bounds for each variable
guess = [4000,6000]  # initial guess where a solution might be
solution = opt.minimize(f_negative, guess  ,constraints=cons, bounds=bnds )
print("\nThe solutions dictionary:")
print(solution)
print("\nValue of variables:", list(solution["x"]), "Max Value of function",-solution["fun"])
    
