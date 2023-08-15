# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 20:27:04 2019

@author: becneljj
"""

def secant_method(f, x0, x1, max_iter=100, tolerance = 1e-5):
    """This function performs the secant root finding method.
    Input: Given a f and intial guess x0 and x1 (root between these)
           max_iter - the number of iterations to try before stopping
           tolerance - the desired level of accurracy
    Output: an approximation to the root of the function (if the method
    converges) """
    steps_taken = 1
    # continue until we hit the max iterations or the accuarcy desired
    while steps_taken < max_iter and abs(x1-x0) > tolerance:
        # solve for the root of the secant
        x2 = x1 - ( (f(x1) * (x1 - x0)) / (f(x1) - f(x0)) )
        x1, x0 = x2, x1 # shift the variables
        steps_taken += 1 # track the iterations
    # end while loop
    return x2



#-------------------------------
def f(val):
    return val**2-2*val

print("The root is approximately", secant_method(f,1,3))

