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

c = np.array([48000,24000,30000,10000,5000,6250])  # negative of objective function
b = [1000,300,5,1] # constraint bounds
A = [[360, 120, 180, 75, 25, 37.5],
     [96, 24, 36, 20, 5, 7.5], 
     [1, 1,1, 0, 0, 0],
     [0, 0, 0, 1, 1, 1]]  # constraints
x1_bnds =(0, 5) # bounds on x1
x2_bnds = (0,5) # bounds on x2
x3_bnds = (0,5) # bounds on x2
x4_bnds =(0, 1) # bounds on x1
x5_bnds = (0,1) # bounds on x2
x6_bnds = (0,1) # bounds on x2


result = opt.linprog(-c,A_ub=A, b_ub=b, bounds=(x1_bnds,x2_bnds, x3_bnds,x4_bnds,x5_bnds,x6_bnds))
print("The result from linprog is\n", result.x, "\nwith a max of", -result.fun)

x1_bnds=(0,1)
result = opt.linprog(-c,A_ub=A, b_ub=b, bounds=(x1_bnds,x2_bnds, x3_bnds,x4_bnds,x5_bnds,x6_bnds))
print("\nD: The result from linprog is\n", result.x, "\nwith a max of", -result.fun)
#

x1_bnds=(2,5)
result = opt.linprog(-c,A_ub=A, b_ub=b, bounds=(x1_bnds,x2_bnds, x3_bnds,x4_bnds,x5_bnds,x6_bnds))
print("\nU: The result from linprog is\n", result.x, "\nwith a max of", -result.fun)

x1_bnds=(0,0)
result = opt.linprog(-c,A_ub=A, b_ub=b, bounds=(x1_bnds,x2_bnds, x3_bnds,x4_bnds,x5_bnds,x6_bnds))
print("\nDD: The result from linprog is\n", result.x, "\nwith a max of", -result.fun)

x1_bnds=(1,1)
result = opt.linprog(-c,A_ub=A, b_ub=b, bounds=(x1_bnds,x2_bnds, x3_bnds,x4_bnds,x5_bnds,x6_bnds))
print("\nDU: The result from linprog is\n", result.x, "\nwith a max of", -result.fun)

x1_bnds=(1,1)
x2_bnds = (0,2) # bounds on x2
result = opt.linprog(-c,A_ub=A, b_ub=b, bounds=(x1_bnds,x2_bnds, x3_bnds,x4_bnds,x5_bnds,x6_bnds))
print("\nDUD: The result from linprog is\n", result.x, "\nwith a max of", -result.fun)


x1_bnds=(1,1)
x2_bnds = (3,5) # bounds on x2
result = opt.linprog(-c,A_ub=A, b_ub=b, bounds=(x1_bnds,x2_bnds, x3_bnds,x4_bnds,x5_bnds,x6_bnds))
print("\nDUU: The result from linprog is\n", result.x, "\nwith a max of", -result.fun)


x1_bnds=(1,1)
x2_bnds = (0,2) # bounds on x2
x4_bnds =(0,0)
result = opt.linprog(-c,A_ub=A, b_ub=b, bounds=(x1_bnds,x2_bnds, x3_bnds,x4_bnds,x5_bnds,x6_bnds))
print("\nDUDD: The result from linprog is\n", result.x, "\nwith a max of", -result.fun)

x1_bnds=(1,1)
x2_bnds = (0,2) # bounds on x2
x4_bnds =(1,1)
result = opt.linprog(-c,A_ub=A, b_ub=b, bounds=(x1_bnds,x2_bnds, x3_bnds,x4_bnds,x5_bnds,x6_bnds))
print("\nDUDU: The result from linprog is\n", result.x, "\nwith a max of", -result.fun)

x1_bnds=(1,1)
x2_bnds = (0,1) # bounds on x2
x4_bnds =(0,0)
result = opt.linprog(-c,A_ub=A, b_ub=b, bounds=(x1_bnds,x2_bnds, x3_bnds,x4_bnds,x5_bnds,x6_bnds))
print("\nDUDDD: The result from linprog is\n", result.x, "\nwith a max of", -result.fun)

x1_bnds=(1,1)
x2_bnds = (2,2) # bounds on x2
x4_bnds =(0,0)
result = opt.linprog(-c,A_ub=A, b_ub=b, bounds=(x1_bnds,x2_bnds, x3_bnds,x4_bnds,x5_bnds,x6_bnds))
print("\nDUDDU: The result from linprog is\n", result.x, "\nwith a max of", -result.fun)
print(result)


#

#
#x1_bnds=(188,None)
#result = opt.linprog(-c,A_ub=A, b_ub=b, bounds=(x1_bnds,x2_bnds, x3_bnds))
#print("\nThe result from right branch is\n", result)
#
#
#x1_bnds=(42,187)
#result = opt.linprog(-c,A_ub=A, b_ub=b, bounds=(x1_bnds,x2_bnds, x3_bnds))
#print("\nThe result from left right branch  is\n", result)
#
#x1_bnds=(0,41)
#result = opt.linprog(-c,A_ub=A, b_ub=b, bounds=(x1_bnds,x2_bnds, x3_bnds))
#print("\nThe result from left left branch  is\n", result)

#-------------shadow price x1---------------------
#dual_problem(A,b,c)

