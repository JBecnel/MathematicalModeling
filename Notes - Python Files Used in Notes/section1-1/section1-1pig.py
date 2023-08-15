# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 20:26:59 2018

@author: becneljj
"""
import numpy as np # numerical calculations in python

#---------------------------plot the function
def f(x):
    return (0.65-0.01*x)*(200+5*x)-0.45*x

import matplotlib.pyplot as plt

plt.figure(1,figsize=(8,5)) # create a figure

# create an array of X and Y values
X = np.linspace(0, 20, 50,endpoint=True)
Y = f(X)

# pot the function and label the axes
plt.plot(X, Y, color="blue", linewidth=2.5, linestyle="-")
plt.xlabel('times (days)')
plt.ylabel('profit in $')

plt.show() # show the plot

#----------------------------find the derivative

import sympy as sym #symbolic calculations in python

x = sym.symbols('x') #sympy declare x as a symbol
fprime_expr =sym.diff(f(x),x) # take the derivative 
print("The expressions for f'(x) is", fprime_expr)


#---------------------------find the extrema

# define a function for fprime
def fprime(x):
    return -0.1*x + 0.8


solution_list = sym.solve(fprime_expr, x)
print("The output from solving f'(x) = 0 is", solution_list)
root =  solution_list[0] # get the first (and only) solution from the list

print("The max is", f(root), "and is located at", root)



