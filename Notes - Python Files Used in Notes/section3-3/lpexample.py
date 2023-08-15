# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 22:51:11 2019

@author: becneljj
"""

import scipy.optimize as opt

c = [-3,-5]  # negative of objective function
b = [4,12,18] # constraint bounds
A = [[1,0], [0,2], [3,2]] # constraints
x1_bnds =(0, None) # bounds on x1
x2_bnds = (0,None) # bounds on x2

result = opt.linprog(c,A_ub=A, b_ub=b, bounds=(x1_bnds,x2_bnds))
print("\nThe result from linprog is\n", result)

print("\n\nThe maximum is", -result["fun"], "at the point", result["x"])
