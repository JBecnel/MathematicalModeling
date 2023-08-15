# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 22:30:34 2018

@author: becneljj
"""
import numpy as np # numerical calculations 
import sympy as sym # for symbolic manipulation
import matplotlib.pyplot as plt # for plotting of mathematical functions

#--------------------------------------------------
def f(x, r=0.01, g = 5.0):
    """ This is the function we are studying where
    where the input x represents time, the output 
    of the function is the profit from selling the pig. 
    We have two parameters, r, the rate at which the price
    per pound for the pig is decreasing, and g, the number
    of lbs. the pig gains per day."""
    return (0.65-r*x)*(200+g*x)-0.45*x



#---------------------------------------------------
#sympy declare x and r as symbols
x = sym.symbols('x') 
r = sym.symbols('r')

dfdx = sym.diff(f(x, r),x) # take the derivative with respect to x
# find a list of critical points by solving when equal to 0
critical_points = sym.solve(dfdx, x)   
print("The derivative is with respect to x is", sym.simplify(dfdx), ".\n")
print("The critical points are", critical_points,".\n")

x_in_terms_of_r = critical_points[0]
print("Thus x as a function of r is x=", x_in_terms_of_r, ".\n" )


#----------------------------------------
# make a function x in terms of r
x_of_r = sym.lambdify(r,x_in_terms_of_r,"numpy")
    
# Let's make a rudimentary table of x versus 
print("r = \t x=")
for val in np.arange(0.005, 0.016, 0.001):
    print( round(val,3), "\t",  round(x_of_r(val),3))


#---------------------------------------------------------

# We make several plots of f for different values of r
X = np.linspace(0, 20, 50,endpoint=True)

# this segment of code plots our profit function
# against time for several values of r

# creates a list of values for r [0.005,...0.15]
r_vals = np.arange(0.005, 0.016, 0.001) 
# create a row of subplots with one subplot for each value of r
fig, axes = plt.subplots(1, len(r_vals))
fig.set_size_inches(50,4)
for i in range(len(r_vals)):
    axes[i].plot(X, f(X,r_vals[i]), linewidth=2.5, linestyle="-")
    axes[i].set_title("r = " +str( r_vals[i]))

plt.show()

#-------------------------------------------------
# we now plot x versus r
plt.figure(2)
# create of a plot of the x values versus the r values
x_vals = x_of_r(r_vals)
plt.plot(r_vals, x_vals)

plt.xlabel('r')
plt.ylabel('x (critical value)')
plt.show()

#-----------------Compute S(x,r)---------------
# take the derivative dx/dr
dxdr = sym.diff(x_in_terms_of_r,r)
print("The derivative dx/dr is",dxdr, "and at r =0.01 the derivative value is", dxdr.subs(r,0.01), "\n")
print("Thus at x=8 and r=0.01 we have S(x,r)=", dxdr.subs(r,0.01)*0.01/8, "\n")


#-----------------Compute S(y,r)---------------------
# substitue the function x in terms of r into the original function f
print("The profit just in terms of r is",sym.simplify( f(x_of_r(r),r)), "\n")
dydr = sym.simplify(  sym.diff(f(x_of_r(r),r),r)) # simplify the expression
print("The value of dy/dr is", dydr, "\n" )
print("Thus at y=133.2 and r = 0.01 we have S(y,r)=", dydr.subs(r,0.01)*0.01/133.2)
#
