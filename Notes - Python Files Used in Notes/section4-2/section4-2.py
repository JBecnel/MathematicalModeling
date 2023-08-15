# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 22:07:10 2019

@author: becneljj
"""
import sympy as sym  # used for symbolic mainpulation of mathematical expressions
import matplotlib.pyplot as plt # used to make fancy plots
import numpy as np # numerical calculations

#------------------------------------------------
# functions for the rate of change
def f1(x1, x2, alpha = 0.7e-7):
    return 0.05*x1*(1-x1/150000.0)-alpha*x1*x2

def f2(x1, x2, alpha = 0.7e-7):
    return 0.08*x2*(1-x2/400000.0)-alpha*x1*x2

#------------------------------------

def plot_vector_field(a = 0.7e-7):
    """ This function plots the vector field for the given dynamical system.
    The plot is supplemented with the functions representing where each rate
    of change is 0. """
    
    plt.figure()
    
    
    # use a sparse mesh for the vector field
    X = np.arange(0, 200000, 20000)
    Y = np.arange(0, 500000, 50000)
    X, Y = np.meshgrid(X,Y)
    
    # plot the vector field
    plt.quiver(X,Y,f1(X,Y, alpha=a),f2(X,Y,alpha=a), units="width")
    
    # plot the one vector at the initial condition
    X = [5000]
    Y = [70000]
    X, Y =np.meshgrid(X,Y)
    plt.quiver(X,Y,f1(X,Y,alpha=a),f2(X,Y,alpha=a), units="width", color="orange")
    
    # use a dense mesh for the plots
    X = np.arange(-3000, 200000, 1000)
    Y = np.arange(-10000, 500000, 1000)
    X, Y = np.meshgrid(X,Y)
    # plot where the functions are 0
    plt.contour(X,Y, f1(X,Y,alpha=a), [0], colors='blue')
    plt.contour(X,Y, f2(X,Y,alpha=a), [0], colors='red')
    
    
    plt.xlabel("x1 (blue whales)")
    plt.ylabel("x2 (fin whales)")
    plt.title("Vector Field and Level Sets")
    
    plt.show()

#-------------------------------------------------------
def sensitivity_alpha(x_expr, alpha_val):
    """This function computes the sensitivity of a variable whose
    given in terms of alpha by the x_expr variable at the alpha value
    given by alpha_val."""
    # find the value of x at the given value of alpha
    x_val = x_expr.subs(a, alpha_val)
    # find the derivative with respect to alpha
    dxda = sym.diff(x_expr, a)
    # compute the sensitivity
    sensitivity = dxda.subs(a,alpha_val)*alpha_val/x_val
    return x_val, sensitivity
    
#========================================================
# symbols used in expressions for derivatives
x1,x2 = sym.symbols("x1,x2")
a = sym.symbols("a")

# plot the dynamic system
plot_vector_field()


# the equilibrium points
solutions = sym.solve([f1(x1,x2,alpha=a), f2(x1,x2,alpha = a)], x1, x2)
# print the solutions
for s in solutions:
    print("\nAn equilibrium point:", s)
    
# find x1 and x2 it terms of alpha at the nontrivial equilibrium
x1_of_a = solutions[-1][0]
x2_of_a = solutions[-1][1]

# let's now solve to figure our for what values of alpha
# we get a solution with nonnegative x1 and x2 values
sol1 = sym.solveset(x1_of_a >=  0, a, domain=sym.S.Reals)
sol2 = sym.solveset(x2_of_a >=  0, a, domain=sym.S.Reals)

print("\n The first coordinate is nonnegative on", sol1)
print("\n The second coordinate is nonnegative on", sol2)
    

# consider alpha in the first interval
plot_vector_field(a=1.0e-7)

# consider alpha in the second interval
plot_vector_field(a=4.0e-7)

# compute the sensitivity for x1 w.r.t to alpha
x1_val, sensitivity_x1 = sensitivity_alpha(x1_of_a, alpha_val=1.0e-7)
print("\n At alpha =", 1.0e-7, "we get x1 =", x1_val, "with a sensitivity of", sensitivity_x1)

# compute the sensitivity for x2 with respect to alpha
x2_val, sensitivity_x2 = sensitivity_alpha(x2_of_a, alpha_val=1.0e-7)
print("\n At alpha =", 1.0e-7, "we get x2 =", x2_val, "with a sensitivity of", sensitivity_x2)
