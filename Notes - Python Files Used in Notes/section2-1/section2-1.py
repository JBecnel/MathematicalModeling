# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 08:39:02 2018

@author: becneljj
"""

import  sympy as sym  # used for symbolic mainpulation of mathematical expressions
import matplotlib.pyplot as plt # used to make fancy plots
from matplotlib import cm # color mapping
import numpy as np # numerical calculations

# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
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

#----------------------------------------------------------------------------
def partial(expr, variable):
    """ This module symbolically takes the partial derivative of given
        expression with respect to the symbol given as a string.
        Input: a sympy expression along with a string for the variable
        Output: an expression for the partial derivative
    """
    x = sym.symbols(variable) # define the symbol x
    return sym.diff(expr,x)    # take the derivative symbolically
    

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
    
    # show the plot
    plt.show()
    

    
#----------------------find_critical_point---------------------------
    
def find_critical_point(expression_for_function, variable1, variable2):
    """This function finds a critical for the given function and returns
    the coordinates where the maximum occurs.
    Input: The function to maximize as an expression and strings representing
    the independent variables in the expression
    Output: The function returns the value of the two variables that maximize 
    the function at a crtical point
    """
    x1 = sym.symbols(variable1)
    x2 = sym.symbols(variable2)

    # find the two partial derivatives
    partial_x1 = partial(expression_for_function,variable1)
    print("The partial with respect to x1 is", partial_x1)
    partial_x2 = partial(expression_for_function,variable2)
    print("The partial with respect to x2 is", partial_x2)
    
    # find the critical point
    solution = sym.solve((partial_x1, partial_x2), x1,x2)
    print(solution)
    print("The maximimum and minimum offer at", variable1, "=",solution[x1], "and", variable2,"=", sym.simplify(solution[x2]))
    
    # return the values of the two variables that give us the critical point
    # where the maximum occurs
    return solution[x1], solution[x2]



        
#----------------------sensitivity_analysis----------------

def sensitivity_analysis_for_a(val_x1, val_x2, a =0.01):
    x1 = sym.symbols("x1")
    x2 = sym.symbols("x2")
    a = sym.symbols("a")
    expr_for_f = sym.simplify(f(x1,x2,a))
    print("The simiplied expression for f is", expr_for_f)
    #print("The derivative with respect to x1 is",partial(expr_for_f,"x1"))
    #print("The derivative with respect to x2 is",partial(expr_for_f,"x2"))
    x1_in_terms_of_a, x2_in_terms_of_a = find_critical_point(expr_for_f,"x1","x2")
    print("The absolute maximum is at y=", sym.simplify(f(x1_in_terms_of_a, x2_in_terms_of_a)))
    
    x1_of_a = sym.lambdify(a,x1_in_terms_of_a,"numpy")
    x2_of_a = sym.lambdify(a,x2_in_terms_of_a,"numpy")
    
    # plot x1 versus a to get an idea of how x1 is changing
    plt.figure(3)
    A = np.linspace(0.005, 0.02, 20, endpoint=True)
    plt.plot(A, x1_of_a(A))
    plt.xlabel("a")
    plt.ylabel("x1 (19 inch TVs)")
    plt.title("x1 in terms of a")
    plt.show()
    
    # find the derivative w.r.t to a
    dx1da = sym.diff(x1_in_terms_of_a, a)
    print("The derivative dx1/da is", dx1da)
    print("The derivative dx1/dx at a = 0.01 is",dx1da.subs(a,0.01))
    print("The value of S(x1,a) is", dx1da.subs(a,0.01)*0.01/val_x1)

    # plot x2 versus a to get an idea of how x2 is changing
    plt.figure(4)
    A = np.linspace(0.005, 0.02, 20, endpoint=True)
    plt.plot(A, x2_of_a(A))
    plt.xlabel("a")
    plt.ylabel("x2 (21 inch TVs)")
    plt.title("x2 in terms of a")
    plt.show()
    
    dx2da = sym.diff(x2_in_terms_of_a, a)
    print("The derivative dx2/da is",sym.simplify( dx2da))
    print("The derivitave dx2/dx at a = 0.01 is",dx2da.subs(a,0.01))
    print("The value of S(x2,a) is", dx2da.subs(a,0.01)*0.01/val_x2)
    
    # plot y versus a to get an idea of how y is changing
    plt.figure(5)
    plt.plot(A, f(x1_of_a(A),x2_of_a(A),a=A))
    plt.xlabel("a")
    plt.ylabel("y Profit")
    plt.title("y in terms of a")
    plt.show()
    
    
    dyda = sym.diff(f(x1,x2,a),a)
    print("The derivative dy/da is", dyda)
    print("The derivative dy/da at a = 0.01 is",dyda.subs([(x1,val_x1), (x2,val_x2), (a,0.01)]))
    print("The value of S(y,a) is", dyda.subs([(x1,val_x1), (x2,val_x2), (a,0.01)])*0.01/f(val_x1,val_x2))
   
#--------------------------robustness----------------------
def robustness(original_s, original_t, new_a):
    x1 = sym.symbols("x1")
    x2 = sym.symbols("x2")    
    expr_for_f = sym.simplify(f(x1,x2, a=new_a))
    
    s,t = find_critical_point(expr_for_f, "x1", "x2")
    max_profit = f(s,t,a=new_a)
    print("The maximum profit is",max_profit )
    model_profit = f(original_s,original_t,a=new_a )
    print("Using our original model the profit would be", model_profit)
    print("The percent difference is given by",(max_profit-model_profit)/max_profit)

#============================START===========================

# find a simplified expression for f
x1 = sym.symbols("x1")
x2 = sym.symbols("x2")
expr_for_f = sym.simplify(f(x1,x2))
print("Here is a simplified expression for f(x1,x2)=", expr_for_f)

#  plot the function profit function on a 0-10000 square grib 
plot_function_and_contour(0,10000)

# Find the critical point and the maximum
s,t = find_critical_point(expr_for_f,"x1","x2")
print("The absolute maximum is at y=", f(s,t))
    
# display the expected revenue, price of tv sets, profit margin
print("\nThe expected revenue is", revenue(s,t))
print("The average price of the 19-inch set", price19(s,t))
print("The average price of the 21-inch set", price21(s,t))
print("The profit margin is", revenue(s,t)/profit(s,t), "\n")

#we now perform sensitivity analysis on parameters of interest
sensitivity_analysis_for_a(s,t)

#robustness of our model w.r.t to a
print("\nRobustness with respect to a")
robustness(s,t, 0.011)