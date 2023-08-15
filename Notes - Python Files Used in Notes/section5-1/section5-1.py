# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 15:10:36 2019

@author: becneljj
"""

import sympy as sym
from numpy import linalg as la
from scipy import linalg as spla
import numpy as np
import matplotlib.pyplot as plt

#---------------------------------------------------------------------------
def f1(x1,x2, t=0.5):
    """This function returns the rate of change in population 1
    given the values of two popluations and a parameter t representing 
    the relationship between competition among the same species and different spcies.
    The default values is 0.5 which says we expect half the amount of competition
    between species and among the same species."""
    r1 = 0.10 # growth rate of species 1
    a1 = r1/10000 # competition rate between same species 1
    b1 = t*a1 # competitiion rate between different spaces as
    # a percentage of the rate between same species

    return r1*x1-a1*x1**2-b1*x1*x2

#------------------------------------------------------------------------
def f2(x1,x2, t=0.5):
    """This function returns the rate of change in population 2
    given the values of two popluations and a parameter t representing 
    the relationship between competition among the same species and different spcies.
    The default values is 0.5 which says we expect half the amount of competition
    between species and among the same species."""
    r2 = 0.25 # growth rate of species 1
    a2 = r2/6000 # competition rate between same species 1
    b2 = t*a2 # competitiion rate between different spaces as
    # a percentage of the rate between same species
    return r2*x2-a2*x2**2-b2*x1*x2


def plot_vector_field(t = 0.5):
    """ This function plots the vector field for the given dynamical system.
    The plot is supplemented with the functions representing where each rate
    of change is 0. """
    
    plt.figure(1)
    
    
    # use a sparse mesh for the vector field
    X = np.arange(0, 12000, 1000)
    Y = np.arange(0, 7000, 1000)
    X, Y = np.meshgrid(X,Y)
    
    # plot the vector field
    plt.quiver(X,Y,f1(X,Y, t),f2(X,Y,t), units="width")
    
    # plot the one vector at the initial condition
    #X = [5000]
    #Y = [70000]
    #X, Y =np.meshgrid(X,Y)
    #plt.quiver(X,Y,f1(X,Y,alpha=a),f2(X,Y,alpha=a), units="width", color="orange")
    
    # use a dense mesh for the plots
    X = np.arange(0, 12000, 100)
    Y = np.arange(0, 7000, 100)
    X, Y = np.meshgrid(X,Y)
    # plot where the functions are 0
    plt.contour(X,Y, f1(X,Y,t), [0], colors='blue')
    plt.contour(X,Y, f2(X,Y,t), [0], colors='red')
    
    
    plt.xlabel("x1 (hardwoods)")
    plt.ylabel("x2 (softwoods)")
    plt.title("Vector Field and Level Sets")
    
    plt.show()


#-------------------------------------------------------------------------
def find_equilibrium(eq1, eq2, variable_list):
    """This method solves a given system of equations finding the points (x1,x2)
    where the equations are 0. The solutions are priinted and returned"""
    
    # find the solutions to the equation
    solutions = sym.solve([eq1,eq2],variable_list)

    # print the solutions line by lien
    for s in solutions:
        print("\nA equilibrium solution is:", s)
        
    return solutions

#--------------------------------------------------------------------
def find_jacobian(x1_val, x2_val, t=0.5, numeric=False):
    """This method returns an expression for the partial derivative at the given variable."""
    J = [ ] 
    for f in [f1,f2]: # for each function
        row = [ ]     # row of partial for each function
        for x in [x1,x2]: # for each variable
            partial = sym.diff(f(x1,x2,t), x) # find the partial
            partial_evaluated = partial.subs([(x1,x1_val),(x2,x2_val)])
            
            # convert the partial to a float if we want a numeric answer
            if (numeric):
                row.append(float(partial_evaluated)) # add it to the row
            else: # otherwise leave the partial as an expression
                row.append(sym.simplify(sym.nsimplify(partial_evaluated, rational = True)))
            # end for x
        J.append(row) # when the row is finished add the row to the Jacobian
    # end for f
    
    return J

#------------------------------------------------------------------------
def senstivity_analysis():
    """This method performs steps required for sensitiivty analysis on the parameter t"""
    t = sym.symbols("t")    

    # find the equilbrium in terms of t
    solutions = find_equilibrium(f1(x1,x2,t), f2(x1,x2,t), [x1,x2])
    eq_point=solutions[3] # get the one that is non zero on both terms
    
    print("\nThe equlibrium is ", eq_point)
    
    J= find_jacobian(x1,x2,t)
    print("\nThe jacobian is ", J)
    
    J = find_jacobian(eq_point[0], eq_point[1], t)
    print("\nThe Jacobian at the equilibrium is", J)
    
    J = sym.Matrix(J)
    eigen_dict = J.eigenvals()
    eigen_list = list(eigen_dict.keys())
    print("\n The eigenvalue list is : ", eigen_list)
    
    
    # make both eigenvalue expressions in functions      
    eig1 = sym.lambdify(t,eigen_list[0],"numpy")
    eig2 = sym.lambdify(t,eigen_list[1],"numpy")
    
    # plot the eigenvalues on [0,0.6] using different colors.
    plt.figure(1)        
    t_vals = np.linspace(0, 0.6, 30, endpoint=True)
    lambda_vals1 = eig1(t_vals)
    plt.plot(t_vals, lambda_vals1)

    lambda_vals2 = eig2(t_vals)
    plt.plot(t_vals, lambda_vals2, color="red")

    plt.xlabel('t')
    plt.ylabel('lambda (eigenvalues)')
    plt.show()
    
 #========================MAIN======================================
    
# symbols used in equilibrium equations
x1, x2 = sym.symbols("x1,x2")


# find all the equilibrium solutions
solutions = find_equilibrium(f1(x1,x2), f2(x1,x2), [x1,x2])
eq_point=solutions[2] # get the one that is non zero on both terms

# plot the vector field
plot_vector_field()


J =  find_jacobian(eq_point[0], eq_point[1], numeric=True)
print("\n\nJacobian numerical =", J)

print("\n\nThe eigenvalues from numpy are", la.eigvals(J))
print("The eigenvalues from scipy are", spla.eigvals(J))

# find the eigenvalues using sympy
J = sym.Matrix(J) # turn J into a sympy matrix
print("\n The eigenvalues from \n", sym.nsimplify(J, rational=True)  ,"with sympy are \n", J.eigenvals())

# symbolic Jacobian
J_sym =  find_jacobian(x1,x2)
print("\n\nJacobian symbolic: ",J_sym)
J_sym = sym.Matrix(J_sym)
print("\n\n The eigevalues are: ",  J_sym.eigenvals())

# perform sensitivity analysis
senstivity_analysis()