# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 22:30:34 2018

@author: becneljj
"""
import numpy as np
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
#sympy declare x and g as symbols
x = sym.symbols('x') 
g = sym.symbols('g')

dfdx = sym.diff(f(x, g=g),x) # take the derivative with respect to x
# find a list of critical points by solving when equal to 0
critical_points = sym.solve(dfdx, x)   
print("The derivative is with respect to x is", sym.simplify(dfdx), ".\n")
print("The critical points are", critical_points,".\n")

x_in_terms_of_g = critical_points[0]
print("Thus x as a function of g is x=", x_in_terms_of_g, ".\n" )


#----------------------------------------
# make a function x in terms of g
x_of_g = sym.lambdify(g,x_in_terms_of_g,"numpy")
    
# Let's make a rudimentary table of x versus g 
print("g = \t x=")
for val in np.arange(3, 8, 0.5):
    print( round(val,3), "\t",  round(x_of_g(val),3))


#---------------------------------------------------------

# We make several plots of f for different values of g
X = np.linspace(0, 20, 50,endpoint=True)

# this segement of code plots our profit function
# against time for several values of g

# creates a list of values for g [3, 3.5, 4,...,7.5]
g_vals = np.arange(3, 8, 0.5) 
# create a row of subplots with one subplot for each value of g
fig, axes = plt.subplots(1, len(g_vals))
fig.set_size_inches(50,4)
for i in range(len(g_vals)):
    axes[i].plot(X, f(X,g=g_vals[i]), linewidth=2.5, linestyle="-")
    axes[i].set_title("g = " +str( g_vals[i]))

plt.show()

#-------------------------------------------------
# we now plot x versus g
plt.figure(2)
# create of a plot of the x values versus the g values
x_vals = x_of_g(g_vals)
plt.plot(g_vals, x_vals)

plt.xlabel('g')
plt.ylabel('x (critical value)')
plt.show()

#-----------------Compute S(x,g)---------------
# take the derivative dx/dg
dxdg = sym.diff(x_in_terms_of_g,g)
print("The derivative dx/dg is",dxdg, "and at g =5 the value of the derivative is", dxdg.subs(g,5), "\n")
print("Thus at x=8 and g=5 we have S(x,g)=", dxdg.subs(g,5)*5/8, "\n")


#-----------------Computer S(y,g)---------------------
# substitue the function x in terms of g into the original function f
print("The profit just in terms of g is",sym.simplify( f(x_of_g(g),g=g)), "\n")
dydg = sym.simplify(  sym.diff(f(x_of_g(g),g=g),g)) # simplify the expression
print("The value of dy/dg is", dydg, "\n" )
print("Thus at y=133.2 and g = 5 we have S(y,g)=", dydg.subs(g,5)*5/133.2)


# Let's make a rudimentary table of y versus g 
print("g  \t Optimal Profit \t Profit at 8 days" )
for val in [4.5,5.0,5.5]:
    print( round(val,3), "\t",  f(x_of_g(val),g=val), "\t", f(8, g=val))
