# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 22:04:05 2019

@author: becneljj
"""

import numpy as np
import numpy.linalg as npla


#-----------------------------------------------
# transition matrix
P =np.array([[0,1/3,2/3], [1/2,0,1/2], [3/4,1/4,0]])


# The equation pi P = pi is equivalent to
# (P^T - I)pi^T = 0
C = P.transpose() - np.identity(3)
# we now add the equation pi_1 + pi_2 + pi_3 = 1
C = np.vstack([C, np.ones(3)])
# b will be a vector of 0 0 0 and 1
# the 0 0 0 is from # (P^T - I)pi^T=0
# and the 1 is from pi_1 + pi_2 + pi_3 = 1
b = np.zeros(4)
b[-1] = 1

# Find the least squared solution to Ax = b
# i.e. x that minimizes ||Ax-b||
sol = npla.lstsq(C,b, rcond=None)
pi = sol[0]
error = sol[1]
print("\n\nThe least squares solution is pi", pi, " with sum of residuals", error)

# compute the relative time in each state given that
# the average wait time is 1,2,3 respectively
total = 1*pi[0] + 2*pi[1] + 3*pi[2]

# compute the percent of time spent in each state
print("\nThe percent of time spent in state 1 is", 1*pi[0]/total*100)
print("The percent of time spent in state 2 is", 2*pi[1]/total*100)
print("The percent of time spent in state 3 is", 3*pi[2]/total*100)

#---------------------------------------------------------

# the flow rate matrix along with the constraint p1 +p2+p3=1
A =np.array([[-1,1/4,1/4], [1/3,-1/2,1/12], [2/3,1/4,-1/3],[1,1,1]])
# the right hand side of the steady state equations (0,0,0,1)
b = np.array([0,0,0,1])

sol = npla.lstsq(A,b, rcond=None)
print("\nThe least squares solution to the flow rate equations are ", sol[0], " with sum of residuals", sol[1])
