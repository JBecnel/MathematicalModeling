# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 14:50:29 2019

@author: becneljj
"""

import numpy as np   #numerical calculations
import sympy as sym  # symbolic solver
import scipy.integrate as de # differential equation solver
import matplotlib.pyplot as plt # fancy plotting


#--------------------------------------------------
# These are the dynamic system equations.
def f1(x1,x2):
    return 2*x1-x1*x2

def f2(x1,x2):
    return 4*x2-2*x1*x2

def F(x, t):
    value = [f1(x[0],x[1]), f2(x[0],x[1])]
    return np.array(value)
    
#----------------------------------------------------------------
def euler_method(start_time, end_time, initial_value, num_steps):
    """This method performs Euler's method to approximate a solution to a dynamical
    system. We are given the start time, the end time and the number of steps. 
    These together will tell us the step size. We are also given teh initial value.
    of the system."""
    h = (end_time-start_time)/num_steps  # step size
    
    # list of values for the approximation
    approximation = [initial_value] 
    
    t = start_time # current time in simulation
    point = initial_value; # current point or state of the system
    for k in range(0,num_steps):
        point = point + h * F(point, t) # euler formula
        t = t + h
        approximation.append(point) # add current state to the list
        
    return approximation


#===================================================

start =np.array([1,1])
approx = euler_method(0, 2,start , 4)

print("The approximation to the solution is given by", approx)

x1 = [p[0] for p in approx]
x2 = [p[1] for p in approx]
t = np.linspace(0,2, len(x1))

# plot each variable versus time
plt.plot(t,x1, linestyle ="-", marker="o", color="blue")
plt.plot(t,x2, linestyle ="-", marker="o", color="green")

plt.ylabel("x1, x2")
plt.xlabel("time")
plt.title("Values vs. Time x1 (Green), x2 (Blue)")


plt.show()

plt.figure()
plt.plot(x1,x2, linestyle="--", marker="x",color="red")
plt.xlabel("x1")
plt.ylabel("x2")
plt.title("x1 vs. x2")
plt.show()