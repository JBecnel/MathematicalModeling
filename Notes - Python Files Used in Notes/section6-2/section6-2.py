# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 08:31:22 2019

@author: becneljj
"""

import matplotlib.pyplot as plt # used to make fancy plots
import numpy as np # numerical calculations
import sympy as sym # symbolic calculations
#------------------------------------------------
# functions for the rate of change in x1, blue whale population
def f1(x1, x2, comp_rate = 1.0e-7):
    # competition rate between species defaults to 10^-7
    return 0.05*x1*(1-x1/150000.0)-comp_rate*x1*x2

# functions for the rate of change in x2, fin whale population
def f2(x1, x2, comp_rate = 1.0e-7):
    # competition rate between species defaults to 10^-7
    return 0.08*x2*(1-x2/400000.0)-comp_rate*x1*x2

# same as above, but in vector form using np.arrary
# x - is an np.array (vector) representing the current state
def F(x, comp_rate = 1.0e-7):
    return np.array([f1(x[0],x[1], comp_rate),f2(x[0],x[1], comp_rate) ])

#-----------------------------------------------------------------------

def find_equilibrium(comp_rate = 1.0e-7):
    """This funciton finds the nontrivial equilibrium of the system (both value nonzero) 
    and returns the equilbrium point."""
    
    # the equilibrium points
    x1 = sym.symbols("x1")
    x2 = sym.symbols("x2")
    solutions = sym.solve([f1(x1,x2,comp_rate), f2(x1,x2,comp_rate)], x1, x2)
    # print the solutions
    equil_point = [ 0,0]
    for s in solutions:
        if(s[0]>0) and (s[1] > 0):
            return s
    
    return equil_point
#------------------------------------------
def simulate_population(comp_rate = 1.0e-7, start = np.array((5000,70000)), max_years = 800, epsilon=100):
   """This is method creates a sequences of points demonstrating how our
   discrete time dynamical system is changing. We begin at the starting 
   position given by start (the population of blue and fin whales) 
   an numpy array (vector). The system is run up to the maximum number of
   steps given by max years or until both populations reach within epsilon
   of the equilibrium.
   
   A list of tuples representing the states we traversed is returned 
   along with the final winner sate.
   """
   # list of points that will be return 
   point_list = [  ]
   current_point = start # loop variable holding the current state of system
   
   # find the nontrivial equilibrium solution for the system
   equilibrium = find_equilibrium(comp_rate)
   
   blue_year = max_years # year the blue whales reached near equilibrium (or max population)
   fin_year = max_years # year the fin whales reached near equilibrium (or max population)
   
   # we continue the simulation until we reach the max time steps   
   for time_step in range(1,max_years+1):
       point_list.append(tuple(current_point))
       # move to the next point in the system
       current_point = current_point + F(current_point, comp_rate)
       
       # determine if the populations are near the equilibrium for the first time
       # if so record the year
       if (equilibrium[0]-current_point[0] < epsilon) and (blue_year==max_years):
           blue_year = time_step
           
       if (equilibrium[1]-current_point[1] < epsilon) and (fin_year==max_years):
           fin_year = time_step
      
   # return  the sequence of points and the years where each popluation
   # reach near equilibrium or the max population
   return blue_year,fin_year, point_list 

#----------------------------------------------------------------------
    
def population_plot(points, comp_rate=1e-7):
    """ This function plots the population of the the two species of whales
    over time."""
    # get the x1 and x2 values for the points
    x1 = [p[0] for p in points]
    x2 = [p[1] for p in points]
       
    
    # plot the blue whale population vs time
    plt.figure()
    plt.plot(x1, linestyle ="-", color="blue")
    plt.ylabel("x1 (blue whales)")
    plt.xlabel("time (in years)")
    plt.title("Blue Whale Population alpha=" + str(comp_rate))
    
    plt.show()
    
    # plto the find whale population vs time
    plt.figure()
    plt.plot(x2, linestyle ="-", color="green")
    plt.ylabel("x2 (fin whales)")
    plt.xlabel("time (in years)")
    plt.title("Fin Whale Population alpha="+ str(comp_rate))
    
    
    plt.show()
    
#---------------------------------------------------------------------------
def sensitivity_analysis():
    """ This function reruns the simulation for several values of alpha so we can 
    do sensitivyt analysis."""
    table = [ ]
    for alpha in [1e-7,  5e-8, 1e-8, 1e-9]:
        blue_year, fin_year, points = simulate_population(comp_rate=alpha)
        table.append([alpha, blue_year, fin_year])
        population_plot(points, alpha)
        
    # display the table
    print("Alpha  \t Blue \t Fin")
    for t in table:
        print(t[0], "\t", t[1], "\t", t[2])
        
        
#===========================START===============================
    

# simulate the whale population over time
blue_year, fin_year, points = simulate_population()


# display the population statisitics
# the final population will be in the last point returned by the simulatoin
print(" The blue whales reach equilibrium (or max population) after", blue_year)
print(" The pin whales reach equilibrium (or max population) after", fin_year)
print(" Final number of blue whales", points[-1][0])
print(" Final number of fin whales", points[-1][1])

# plot each popluation over time
population_plot(points)

# check the sensitivity analysis
sensitivity_analysis()
