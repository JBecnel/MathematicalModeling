# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 22:51:11 2019

@author: becneljj
"""

import scipy.optimize as opt
import numpy as np

def dual_problem(A,b,c):
    dual_c = b
    dual_b = -1.0 * c
    dual_A = -1.0 * np.transpose(A)
    
    result = opt.linprog(dual_c,A_ub=dual_A, b_ub=dual_b, bounds=(x1_bnds,x2_bnds, x3_bnds))
    print("\n \n", result)

c = np.array([7,3])  # negative of objective function
b = [30,48] # constraint bounds
A = [[2, 5], [8, 3]]  # constraints
x1_bnds =(0, None) # bounds on x1
x2_bnds = (0,None) # bounds on x2

result = opt.linprog(-c,A_ub=A, b_ub=b, bounds=(x1_bnds,x2_bnds))
print("\nThe result from linprog is", result.x, "with a max of", -result.fun)

x1_bnds=(0,4)
result = opt.linprog(-c,A_ub=A, b_ub=b, bounds=(x1_bnds,x2_bnds))
print("\nU: The result from linprog is", result.x, "with a max of", -result.fun)

x1_bnds=(5,None)
result = opt.linprog(-c,A_ub=A, b_ub=b, bounds=(x1_bnds,x2_bnds))
print("\nD: The result from linprog is", result.x, "with a max of", -result.fun)

x1_bnds=(5,None)
x2_bnds=(0,2)
result = opt.linprog(-c,A_ub=A, b_ub=b, bounds=(x1_bnds,x2_bnds))
print("\nUD: The result from linprog is", result.x, "with a max of", -result.fun)

x2_bnds=(3,None)
result = opt.linprog(-c,A_ub=A, b_ub=b, bounds=(x1_bnds,x2_bnds))
print("\nUU: The result from linprog is", result.x, "with a max of", -result.fun)


x1_bnds=(6,None)
x2_bnds=(0,2)
result = opt.linprog(-c,A_ub=A, b_ub=b, bounds=(x1_bnds,x2_bnds))
print("\nUDU: The result from linprog is", result.x, "with a max of", -result.fun)

x1_bnds=(5,5)
result = opt.linprog(-c,A_ub=A, b_ub=b, bounds=(x1_bnds,x2_bnds))
print("\nUDD: The result from linprog is", result.x, "with a max of", -result.fun)

#-------------shadow price x1---------------------
#dual_problem(A,b,c)

