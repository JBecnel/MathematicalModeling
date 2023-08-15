# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 22:51:11 2019

@author: becneljj
"""

import scipy.optimize as opt
import numpy as np



#------------------------------------------------------
def dual_problem(A,b,c):
    """This problem solve the dual of an LP problem: Maximize c.x subject to Ax <= b with x>=0.
    That is, it solves Minimize b.y subject to A^Ty >= c, y >=0.
    The solution to the dual is the shadow price (dual prices)"""
    dual_c = b
    # We change A^Ty >= c to -A^Ty <= c to feed into linprog
    dual_b = -1.0 * c
    dual_A = -1.0 * np.transpose(A)
    
    y1_bnds =(0, None) # bounds on y1
    y2_bnds = (0,None) # bounds on y2
    y3_bnds = (0,None) # bounds on y3

    result = opt.linprog(dual_c,A_ub=dual_A, b_ub=dual_b, bounds=(y1_bnds,y2_bnds, y3_bnds))
    
    return result
#-------------------------------------------------------

    
    
#========================START===========================
# set up LP problem: Maximize c.x subject to Ax <= b with x>=0    
c = np.array([400,200,250])  # negative of objective function
b = [1000,300,625] # constraint bounds
A = [[3, 1, 1.5], [0.8, 0.2, 0.3], [1, 1,1]]  # constraints
x1_bnds =(0, None) # bounds on x1
x2_bnds = (0,None) # bounds on x2
x3_bnds = (0,None) # bounds on x2


result = opt.linprog(-c,A_ub=A, b_ub=b, bounds=(x1_bnds,x2_bnds, x3_bnds))
print("\nThe result from linprog is\n", result)
print("\n\nThe maximum is", -result["fun"], "at the point", result["x"])

# find the shadow prices by solving the dual problem
dual_result = dual_problem(A,b,c)
print("\nThe result of linprog on the daul is\n", dual_result)
print("\n\nThe shadow prices for this problem are", dual_result["x"])

corn_c = c + np.array([50,0,0])
corn_result = opt.linprog(-corn_c,A_ub=A, b_ub=b, bounds=(x1_bnds,x2_bnds, x3_bnds))
print("\nThe result of linprog on the corn change is\n", corn_result)
print("\n\nThe shadow prices for this problem are", dual_problem(A,b,corn_c)["x"])


oat_c = c + np.array([0,0,10])
oat_result = opt.linprog(-oat_c,A_ub=A, b_ub=b, bounds=(x1_bnds,x2_bnds, x3_bnds))
print("\nThe result of linprog on the corn change is\n", oat_result)
print("\n\nThe shadow prices for this problem are", dual_problem(A,b,oat_c)["x"])

mid_point = 0.5*(result.x + oat_result.x)
print("At the midpoint of", mid_point, "the optimal solution",mid_point[0]*c[0]+mid_point[1]*c[1]+mid_point[2]*c[2])