# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 22:39:14 2019

@author: becneljj
"""

import sympy as sym # symbolic mathematical manipulation
import matplotlib.pyplot as plt # used to make fancy plots
import numpy as np # numerical calculations


#------------------------------------------------
def G(x1,x2, k=0.2):
    return (1-10*k)*x1-5*k*x2, x1

#-----------------------------------------------------
def plot_eigenvalues(a,b):
    plt.figure() # we create one figure 

    # the following creates an array of X and Y values
    # the x values start at a and go to b
    X = np.linspace(a, b, 50,endpoint=True)
    Y1 = lambda1(X) # the y-values are computed using the function
    Y2 = lambda2(X)
    
    plt.plot(X, Y1, color="blue", linewidth=2.5, linestyle="-")
    
    
    plt.plot(X, Y2, color="red", linewidth=2.5, linestyle="-")
    plt.xlabel('k')
    plt.ylabel('eigenvalues')
    
    plt.legend(('lambda 1', 'lambda 2'))
    plt.title("k from " + str(round(a,4)) + " to " + str(round(b,4)))
    plt.show()

#===============================START=================================
# find the eigenvalues of the Jacobian
J_G = sym.Matrix([[0.8,-0.1], [1,0]])
eigen_dict = J_G.eigenvals()
eigen_list = list(eigen_dict.keys())
print("\n The eigenvalue list is : ", eigen_list, "or ", sym.N(eigen_list[0]), "and", sym.N(eigen_list[1]))


# find the eigenvalues of the Jacobian
k = sym.symbols("k")
J_G = sym.Matrix([[1-10*k,-5*k], [1,0]])
eigen_dict = J_G.eigenvals()
eigen_list = list(eigen_dict.keys())
print("\n The eigenvalue list is : ", eigen_list)


# find when the eigenvalues are real
# by solving for the discriminate = 0
discriminant = 100*k**2-40*k+1
solutions = sym.solve(discriminant, k)
print("\nThe discriminant is 0 when k is ", solutions, "or ", sym.N(solutions[0]), "and", sym.N(solutions[1]))

# make function from the eigenvalues
lambda1 = sym.lambdify(k, sym.Abs(eigen_list[0]))
lambda2 = sym.lambdify(k, sym.Abs(eigen_list[1]))

k1 = float(sym.N(solutions[0]))
k2 = float(sym.N(solutions[1]))
plot_eigenvalues(0, k1)
plot_eigenvalues(k2, 1)

# note for complex eigenvalues discriminate is negative, so we make it positive
complex_modulus =  (1/2-5*k)**2 - discriminant/4
print(discriminant)
print(complex_modulus)
print(sym.simplify(complex_modulus))
print(sym.solveset(complex_modulus < 1,k, sym.S.Reals))    