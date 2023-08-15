# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import scipy.stats as stat
import scipy.optimize as opt
import numpy as np


#-----------------------------------------------------------------

def graph_norm_dist(mean, std, value):
    """The function graphs a normal pdf with the given mean and
    standard deviation (std). It also marks the given value with
    a vertical line."""
    
    # create a normal distribution
    dist = stat.norm(mean, std)
    
    # let X go 3 standard deviations on each side of the mean
    X = np.linspace(mean-3*std,mean+3*std, num = 100, endpoint=True)
        
    plt.plot(X, dist.pdf(X)) # plot the bell curve
    
    plt.axvline(x=value, color='red') # plot a vertical line
    plt.show()

#--------------------------------------------------------------
    
def find_mean_std_exp(lamb = 0.1):
    # This function return the mean and standard deviation of the
    # exponetial distribution with parameter lamb (lambda).
    exp_dist = stat.expon(scale = 1/lamb) # create exp dist.
    mean = exp_dist.mean()  # get the mean
    std = exp_dist.std() # get the standard deviation
    return mean, std  # return the value

#--------------------------------------------------------------

def prob_sample_avg(mean, std, n, value):
    """This function find the probability of the sample avg Xbar
    for n i.i.d. random varables with the given mean and standard devation
    (std). The probability the average is above and below the given value
    is returned."""
    
    # create a normal distribution for the Xbar
    norm_dist =stat.norm(mean,std/np.sqrt(n))
    # use the cdf to find P(Xbar <= value)
    prob_below = norm_dist.cdf(value)
    # complement rule
    prob_above = 1- prob_below
    
    return prob_above, prob_below
    
#---------------------------------------------------------------
def prob_above(n=153, lamb = 171):
    # create a normal distirbution with the necessary statstics
    norm_dist =stat.norm(1/lamb,1/(lamb *np.sqrt(n)))
    
    # survival function (1-cdf)
    prob_above = norm_dist.sf(1/n)
    
    return prob_above

    
#-----------------------------------------
#def x_score(n):
#    # find the z score using a standard normal distribution
#    std_norm = stat.norm()
#    z_score = std_norm.ppf(0.95)
#    
#    # return value of n
#    return n+z_score*np.sqrt(n)-171
#
#def sensitivity_n(prob=0.05):
#    """This function does a densitivity analysis on the observed value
#    of n. We attempt to figure out what observed value with 
#    gives us a statistically signficiant outcome at the 5% level. """
#    sol=opt.brentq(x_score,100,200)
#    return sol
#


#def solve_n(n, prob=0.05):
#    # create a normal distribution for the Xbar
#    lamb = 171.0
#    norm_dist =stat.norm(1/lamb,1/(lamb *np.sqrt(n)))
#    # use the cdf to find P(Xbar <= value)
#    prob_above = norm_dist.sf(1/n)
#    
#    return prob_above-prob
#
#def solve_lambda(lamb, prob=0.05):
#    # create a normal distribution for the Xbar
#    n = 153.0
#    norm_dist =stat.norm(1/lamb,1/(lamb *np.sqrt(n)))
#    # use the cdf to find P(Xbar <= value)
#    prob_above = norm_dist.sf(1/n)
#    
#    return prob_above-prob


#=======================START=============================
lamb = 171  # parameter for the exponential distribution
mean, std = find_mean_std_exp(lamb)
print("The mean and standard deviation of Xn is", mean, std)

n = 153  # sample size
value = 1/153 # conjectured value of Xbar (sample mean)
prob_right, prob_left = prob_sample_avg(mean, std, n, value)
print("\nThe probability we are above the value is", prob_right)
print("The probability we are below the value is", prob_left)

# graph the normal distiribution and the value we are interested in
graph_norm_dist(mean, std/np.sqrt(n), value)

# create and solve the prob above function for n at a value of 0.05
Pn = lambda n : prob_above(n, 171) -0.05
print("\nThe value of n that produces a signficant result is: ", opt.brentq(Pn, 100,200 ))

# create and solve the prob above function for \lambda at a value of 0.05
Plam = lambda x : prob_above(153,x)-0.05
print("\nThe value of lambda that produces a signficant result is: ", opt.brentq(Plam, 100,200))


#sol_n = sensitivity_n()
#print("The observed value that is statistically signficant is", sol_n)
#
#print(opt.brentq(solve_n, 100,200))
#print(opt.brentq(solve_lambda, 100,200))
