# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 18:09:04 2019

@author: becneljj
"""

import scipy.stats as stat
import numpy as np
import numpy.linalg as npla
import matplotlib.pyplot as plt


#---------------------------------------------------------------
def transition_matrix(mean =1):
    """This function creates the transition matrix in accordance with the
    probability found in the slides. That is, we use the probability
    mass function (pmf) of the Poisson distribution with the given mean."""
    P =np.array([[stat.poisson.pmf(0,mean),0, 1-stat.poisson.pmf(0,mean)], 
              [stat.poisson.pmf(1,mean),stat.poisson.pmf(0,mean),1-stat.poisson.pmf(0,mean)-stat.poisson.pmf(1,mean)], 
              [stat.poisson.pmf(2,mean),stat.poisson.pmf(1,mean),1-stat.poisson.pmf(1,mean)-stat.poisson.pmf(2,mean)]])
    return P

#---------------------------------------------------------------
def iterate(P, initial_state=[0,0,1], num_steps=10):
    """This function iterate the distribution states starting at the
    given initial state for the specified number of steps. The required input
    of this function is the transition matrix P."""
    pi = [] # list to hold the distriubiton states
    pi.append(initial_state) # add the intial state
    
    print("initial state", pi[0])
    for k in range(0,num_steps):
        next_state = pi[k] @ P # pi(k+1) = pi(k) P
        pi.append( next_state) # add the state to the list
        print("state", k+1, "is", next_state) # print the current state

#-----------------------------------------------------------------
def steady_state(P):
    """This functions solves the equation pi P = pi along with the 
    constraint pi_1 + pi_2 + pi_3 =1 to find the steady state distribution
    for the Markov chain given. The required input is the transition matrix for
    the Markov chain given by P."""
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
    return sol[0], sol[1] # return solution and residual


#-------------------------------------------------------
def find_prob(pi, mean=1):
    """This function finds the probablity that demand exceeds
    supply, P(D>S). This is computed by way of
    P(D>S) = P(D>1)*P(S=1) + P(D>2)*P(S=2) + P(D>3)*P(S=3)"""
    # find P(D>1), P(D>2), and P(D>3) from the slides
    P_D_3 = 1-stat.poisson.cdf(3,mean)
    P_D_2 = 1-stat.poisson.cdf(2,mean)
    P_D_1 = 1-stat.poisson.cdf(1,mean)
    return pi[0]*P_D_1 + pi[1]*P_D_2 + pi[2]*P_D_3

#--------------------------------------------------------------
def solution(mean = 1):
    """This function performs all 3 steps of finding the solution using
    the given parameter. It finds the transition matrix, using this to find 
    the steady state and from here computes the probability that supply exceeds
    demand."""
    P = transition_matrix(mean)
    pi, error = steady_state(P)
    prob = find_prob(pi, mean)
    
    return prob

#-------------------------------------------------------------
def sensitivity(prob, val =1):
    """This function does a sensitivity analysis on the mean given.
    The default value for the mean is given by val and the original probability
    is given by prob."""
    
    # we first approximate the derivative using f(x+h)-f(x-h)/2h
    h = 0.01
    prob_plus = solution(val+h)    
    prob_minus = solution(val-h) 
    
    dp = (prob_plus-prob_minus)/(2*h)
    
    # we now compute S(p, lambda)
    print("The sensitivity is given by", dp * val/prob)


    # create a plot of the prob. vs. lambda
    L = np.linspace(0.5,1.5, 30)
    P = [solution(x) for x in L]

    plt.figure(1)        
    plt.plot(L, P)

    plt.xlabel('mean')
    plt.ylabel('probability')
    plt.title("Sensitivity Analysis")
    plt.show()


#======================START============================
P = transition_matrix()
print("The transition matrix is: ", P)

print("\nThe results of iteration:")
iterate(P)

pi, error = steady_state(P)
print("\n\nThe least squares solution is pi", pi, " with sum of residuals", error)

prob=find_prob(pi)
print("\nThe probablity demand exceeds supply is", prob )

sensitivity(prob, val=1)