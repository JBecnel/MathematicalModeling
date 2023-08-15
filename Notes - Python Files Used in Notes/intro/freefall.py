# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 11:54:40 2018

@author: becneljj
"""

GRAVITY = -9.8 # constant representing gravity at -9.8 m/s

# we know ask the user how long the object fell
time_falling = float(input("Enter the amount of time the object is falling: "))

# we commute the velocity using the equation v = gt
velocity = GRAVITY*time_falling 
# we commute the distance the object fell using the equation d = gt^2/2
distance = GRAVITY*time_falling**2/2 

print("The object fell a distance of ", distance, "meters and had a final velocity of ", velocity, " meters per second." )