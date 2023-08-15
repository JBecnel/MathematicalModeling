# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 17:41:26 2019

@author: becneljj
"""

import matplotlib.pyplot as plt
import scipy.stats as stat
import scipy.optimize as opt
import numpy as np

#--------------------------------------------------------
def C(x,t):
    """ This function returns a number between 0 and 1 representing the
    relative concentration level of the pollutant at time t (in hours)
    and location x (in km away from plume center)."""
    return 1/np.sqrt(0.5*np.pi *t) * np.exp(-x**2/(0.5*t))

def concentration_in_town(t, v = 3):
    """This represents the concentration level of the pollutant 
    in the town that is 10 km away. An optional argument of wind speed
    of 3 km/s is also available."""
    return C(10-v*t, t)
    

#-------------------------------------------------------------
def plot_concentration(value, safe_level, v = 3):
    """This function plots the graph of the concentration in town, marking
    the given value on the graph. An optional argument of wind speed
    of 3 km/s is also available."""
    T = np.linspace(0.5,10, num = 100, endpoint=True)
        
    plt.plot(T, concentration_in_town(T, v)) 
    plt.title("Concetration in Town")
    plt.xlabel("distance to town")
    plt.ylabel("concentration")
    plt.axvline(x=value, color='red') # plot a vertical line
    plt.axhline(y=safe_level, color='green')
    plt.show()


#------------------------------------------------------------

def find_solution(wind_speed = 3):
    safe_level = 1/20 * C(0,1) # safe level is 1/20 the max level at t=1

    plt.figure()
    # find the maximum concentration in town
    C_neg = lambda t : -concentration_in_town(t, v=wind_speed)
    solution = opt.minimize_scalar(C_neg, bounds=(0.5,10), method="bounded")
    print("The maximum concentration is town occurs at time:",solution["x"])
    
    max_level = concentration_in_town(solution["x"], v=wind_speed)
    print("The max level is town is",max_level/safe_level ,"times the safe level.")
    # plot the concetration in town; mark the max and safe level
    plot_concentration(solution["x"], safe_level)
    
    
    safe = lambda t : concentration_in_town(t, v=wind_speed) - safe_level
    unsafe_time = opt.brentq(safe, 0.5,3.3)
    print("The concencration level becomes unsafe at t=", unsafe_time)
    
    safe_time=opt.brentq(safe, 3.3,10)
    print("The concencration returns to a safe level at t=", safe_time)


#==========================================================
find_solution()

print("\n\n\nSensitivity Analysis for wind speed:")
find_solution(wind_speed=3.03)