# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 11:31:13 2018

@author: becneljj
"""

import scipy.optimize as opt # for minimize function from scipy

import lagrange # my module with lagrange function
    

#==============TEST CODE====================================

# function
def f(X, negate=False):
    sign = 1
    if (negate):
        sign = -1
    return sign*(2*X[0]+5*X[1])

# constraints
def g(X):
    return X[0]**2/16+ X[1]**2/9-1

# our algrebraic solution
solutions = lagrange.lagrange_algebraic(f,[g], var_list=["x","y"])
print("The exact solutions:\n",solutions)

# numerical solution using scipy package
# constraint over which we are maximizing the function
cons = ({'type': 'eq', # eq for equality; ineq for inequality
         'fun' : g},  # constraint of the form =0 or >=0
        )
bnds = ((-10,10),(-10,10)) # bounds for each variable
guess = [2,1]  # initial guess where a solution might be
solution = opt.minimize(f, guess, args=True ,constraints=cons, bounds=bnds )
print("\nThe solutions dictionary:")
print(solution)
print("\nValue of variables:", list(solution["x"]), "Max value of function",-solution["fun"])