# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 22:04:05 2019

@author: becneljj
"""

import numpy as np
import numpy.linalg as npla

pi=[[1,0,0]]  # initial distribution state
# transition matrix
P =np.array([[1/3,1/3,1/3], [0.7,0.3,0.0], [1,0,0]])

num_steps = 12 # number of steps to simulate

print("initial state", pi[0])
for k in range(0,num_steps):
    next_state = pi[k] @ P # pi(k+1) = pi(k) P
    pi.append( next_state) # add the state to the list
    print("state", k+1, "is", next_state) # print the current state

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

# Find the least squared solution to Cx = b
# i.e. x that minimizes ||Cx-b||
sol = npla.lstsq(C,b, rcond=None)
print("\n\nThe least squares solution is pi", sol[0], " with sum of residuals", sol[1])