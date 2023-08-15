# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 20:02:53 2019

@author: becneljj
"""

import scipy.optimize as opt # for minimize function from scipy

import lagrange # my module with lagrange function


#==============Example 2.4====================================

# function
def f(X, negate=False):
    sign = 1
    if (negate):
        sign = -1
    return sign*(X[0]+2*X[1]+3*X[2])

# constraints
def g(X):
    return X[0]**2+ X[1]**2+X[2]**2-3

def g2(X):
    return X[0]-1

# our algrebraic solution
solutions = lagrange.lagrange_algebraic(f,[g2,g], var_list=["x","y","z"])
print("The exact solutions:\n",solutions)

# numerical solution using scipy package
# constraint over which we are maximizing the function
cons = ({'type': 'eq', # eq for equality; ineq for inequality
         'fun' : g2},  # constraint of the form =0 or >=0
        {'type': 'eq',
        'fun' : g})
bnds = ((-5,5),(-4,4),(-5,5)) # bounds for each variable
guess = [2,1,1]  # initial guess where a solution might be
solution = opt.minimize(f, guess, args=True ,constraints=cons, bounds=bnds )
print("\nThe solutions dictionary:")
print(solution)
print("\nValue of variables:", list(solution["x"]), "Max value of function",-solution["fun"])