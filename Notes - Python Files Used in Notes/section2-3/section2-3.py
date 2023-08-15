# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 08:39:02 2018

@author: becneljj
"""

import  sympy as sym  # used for symbolic manipulation of mathematical expressions
import matplotlib.pyplot as plt # used to make fancy plots
from matplotlib import cm # color mapping
import numpy as np # numerical calculations
#from scipy import optimize # used for root finding
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # 
import scipy.optimize as opt # needed for minimization function

import sys # system
sys.path.append('../section2-2/') # helps me find Lagrange
import lagrange # my module with Lagrange symbolic solver
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

def f_list_a(X):
    """ Here we define the function we want to work with.
        Inputs: a list of variables as inputs
        Output: the value (float) of the function at the given input
    """
    a = sym.symbols("a")
    return f(X[0],X[1],a)


def f_negative(X, a=0.01):
    """ Here we define the function we want to work with.
        Inputs: a list of variables as inputs
        Output: the value (float) of the function at the given input
    """
    return -f(X[0],X[1],a)

def constraint(X, c=10000):
    """ This function is a constraint we have on production of the 19 and 
    21 inch sets, X[0] and X[1]"""
    return X[0]+X[1]-c

def constraint_c(X):
    c = sym.symbols("c")
    return constraint(X,c)

  #----------------------sensitivity_analysis----------------

def sensitivity_analysis_for_a(x1_expr, x2_expr, x1_val, x2_val, y_expr):
    a = sym.symbols("a")
    
    # create functions for x1 and x2 and yin terms of a
    x1_of_a = sym.lambdify(a,x1_expr,"numpy")
    x2_of_a = sym.lambdify(a,x2_expr,"numpy")
    y_of_a =sym.lambdify(a,y_expr,"numpy")
    
    # plot x1 versus a to get an idea of how x1 is changing
    plt.figure(1)
    A = np.linspace(0.005, 0.02, 20, endpoint=True)
    plt.plot(A, x1_of_a(A))
    plt.xlabel("a")
    plt.ylabel("x1 (19 inch TVs)")
    plt.title("x1 in terms of a")
    plt.show()
    
    # find the derivative w.r.t to a
    dx1da = sym.diff(x1_expr, a)
    print("The derivative dx1/da is", dx1da)
    print("The derivative dx1/dx at a = 0.01 is",dx1da.subs(a,0.01))
    print("The value of S(x1,a) is", dx1da.subs(a,0.01)*0.01/x1_val)

    # plot x2 versus a to get an idea of how x2 is changing
    plt.figure(2)
    plt.plot(A, x2_of_a(A))
    plt.xlabel("a")
    plt.ylabel("x2 (21 inch TVs)")
    plt.title("x2 in terms of a")
    plt.show()
    
    # find the derivative w.r.t to a
    dx2da = sym.diff(x2_expr, a)
    print("The derivative dx2/da is",sym.simplify( dx2da))
    print("The derivative dx2/dx at a = 0.01 is",dx2da.subs(a,0.01))
    print("The value of S(x2,a) is", dx2da.subs(a,0.01)*0.01/x2_val)
    
    
    # plot y versus a to get an idea of how x2 is changing
    plt.figure(2)
    plt.plot(A, y_of_a(A))
    plt.xlabel("a")
    plt.ylabel("y (profit)")
    plt.title("y in terms of a")
    plt.show()
    
    # find the derivative w.r.t to a
    dyda = sym.diff(y_expr, a)
    y_val = f(x1_val,x2_val)
    print("The derivative dy/da is",sym.simplify( dyda))
    print("The derivative dy/da at a = 0.01 is",dyda.subs(a,0.01))
    print("The value of S(y,a) is", dyda.subs(a,0.01)*0.01/y_val)
    
    
#-----------------------------------------------------------------
def robustness(x1,x2,a=0.011):
    # solve with a=0.011
    #----------------numerical calculations---------------------
    # constraint over which we are maximizing the function
    cons = ({'type': 'eq', # eq for equality; ineq for inequality
         'fun' : constraint}  # constraint of the form =0 or >=0
        )
    bnds = ((0,5000),(0,8000)) # bounds for each variable
    guess = [4000,6000]  # initial guess where a solution might be
    solution = opt.minimize(f_negative, guess, args=a ,constraints=cons, bounds=bnds )
    print("\nThe solutions dictionary:")
    print(solution)
    print("\nValue of variables:", list(solution["x"]), "Max Value of function",-solution["fun"])

    print("\n Value if we use previous solution:", f(x1,x2,a=a))
    print("\n Profit loss of ", (-solution["fun"]-f(x1,x2,a=a))/(-solution["fun"]) )

#-------------------------------------------------------------
def solve_with_c():
    # find a simplified expression for f
    x1 = sym.symbols("x1")
    x2 = sym.symbols("x2")

    expr_for_f = sym.simplify(f(x1,x2))
    print("Here is a simplified expression for f(x1,x2)=", expr_for_f)



    # algebraically solve using Lagrange multipliers
    solution = lagrange.lagrange_algebraic(f_list,[constraint_c], var_list=["x1","x2"])
    x1_expr =sym.simplify( solution[0][0])
    x2_expr =sym.simplify(solution[0][1])
    y_expr = sym.simplify(solution[1])
    L1 = list(solution[2].values())[0]
    print("The exact solutions are at \n x1 = ",  x1_expr, "\n x2=", x2_expr)
    print("The max is y=", y_expr)
    print("The value of lambda is", L1)
 
    return x1_expr, x2_expr, y_expr
    
  #----------------------sensitivity_analysis----------------

def sensitivity_analysis_for_c(x1_expr, x2_expr, x1_val, x2_val, y_expr):
    c = sym.symbols("c")
    
    # create functions for x1 and x2 and yin terms of a
    x1_of_c = sym.lambdify(c,x1_expr,"numpy")
    x2_of_c = sym.lambdify(c,x2_expr,"numpy")
    y_of_c =sym.lambdify(c,y_expr,"numpy")
    
    # plot x1 versus a to get an idea of how x1 is changing
    plt.figure(1)
    C = np.linspace(10000, 10500, 20, endpoint=True)
    plt.plot(C, x1_of_c(C))
    plt.xlabel("c")
    plt.ylabel("x1 (19 inch TVs)")
    plt.title("x1 in terms of c")
    plt.show()
    
    # find the derivative w.r.t to c
    dx1dc = sym.diff(x1_expr, c)
    print("The derivative dx1/dc is", dx1dc)
    print("The derivative dx1/dx at c = 0.01 is",dx1dc.subs(c,10000))
    print("The value of S(x1,c) is", dx1dc.subs(c,10000)*10000/x1_val)

    # plot x2 versus a to get an idea of how x2 is changing
    plt.figure(2)
    plt.plot(C, x2_of_c(C))
    plt.xlabel("c")
    plt.ylabel("x2 (21 inch TVs)")
    plt.title("x2 in terms of c")
    plt.show()
    
    # find the derivative w.r.t to c
    dx2dc = sym.diff(x2_expr, c)
    print("The derivative dx2/dc is",sym.simplify( dx2dc))
    print("The derivative dx2/dx at c = 10000 is",dx2dc.subs(c,10000))
    print("The value of S(x2,c) is", dx2dc.subs(c,10000)*10000/x2_val)
    
    
    # plot y versus a to get an idea of how x2 is changing
    plt.figure(2)
    plt.plot(C, y_of_c(C))
    plt.xlabel("c")
    plt.ylabel("y (profit)")
    plt.title("y in terms of c")
    plt.show()
    
    # find the derivative w.r.t to c
    dydc = sym.diff(y_expr, c)
    y_val = f(x1_val,x2_val)
    print("The derivative dy/dc is",sym.simplify( dydc))
    print("The derivative dy/dc at c = 10000 is",dydc.subs(c,10000))
    print("The value of S(y,c) is", dydc.subs(c,10000)*10000/y_val)
        
#============================START===========================

# find a simplified expression for f
x1 = sym.symbols("x1")
x2 = sym.symbols("x2")
a = sym.symbols("a") 

expr_for_f = sym.simplify(f(x1,x2,a))
print("Here is a simplified expression for f(x1,x2)=", expr_for_f)



# algebraically solve using Lagrange multipliers
solution = lagrange.lagrange_algebraic(f_list_a,[constraint], var_list=["x1","x2"])
x1_expr =sym.simplify( sym.nsimplify(solution[0][0]))
x2_expr =sym.simplify(sym.nsimplify(solution[0][1]))
y_expr = sym.simplify(sym.nsimplify(solution[1]))
L1 = list(solution[2].values())[0]
print("The exact solutions are at \n x1 = ",  x1_expr, "\n x2=", x2_expr)
print("The max is y=", y_expr)
print("The value of lambda is", L1)

# sensitivity analysis for a
solution = lagrange.lagrange_algebraic(f_list,[constraint], var_list=["x1","x2"])
print("The solution with default a=0.01 is x1 and x2", solution[0][0], solution[0][1])
sensitivity_analysis_for_a(x1_expr, x2_expr, solution[0][0],solution[0][1], y_expr)

# robustness for a 
robustness(solution[0][0], solution[0][1])

# analysis for production constraints c
x1_expr, x2_expr, y_expr = solve_with_c() # solve the problem symbolically with c as a symbol
#compute the sensitivity analysis for the variables
sensitivity_analysis_for_c(x1_expr, x2_expr, solution[0][0],solution[0][1], y_expr)
