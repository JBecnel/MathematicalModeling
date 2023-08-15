# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 08:31:22 2019

@author: becneljj
"""

import matplotlib.pyplot as plt # used to make fancy plots
import numpy as np # numerical calculations

#------------------------------------------------
# functions for the rate of change in x1, the red forces in the battle
def f1(x1, x2, advantage = 1.5):
    # blue has an advantage that we default to 1.5
    return -advantage*(0.05*x2+0.005*x1*x2)

# functions for the rate of change in x2, the blue forces in the battle
def f2(x1, x2, advantage = 1.5):
    return -0.05*x1-0.005*x1*x2

# same as above, but in vector form using np.arrary
# x - is an np.array (vector) representing the current state
# of the system and advantage is the multiplier for blue's advantage
# over red forces.
def F(x, advantage =1.5):
    return [f1(x[0],x[1], advantage),f2(x[0],x[1], advantage) ]

    
#------------------------------------------
def simulate_battle(advantage = 1.5, start = np.array((5,2)), max_steps = 60):
   """This is method creates a sequences of points demonstrating how our
   discrete time dynamical system is changing. We begin at the starting 
   position given by start (the number of blue and red forces) 
   an numpy array (vector). The system is run up to the maximum number of
   steps given by max points or until one of the forces drops to 0
   
   A list of tuples representing the states we traversed is returned 
   along with the final winner sate.
   """
   # list of points that will be return 
   point_list = [  ]
   current_point = start # loop variable holding the current state of system
   
   time_step = 1
   # we continue the battle until we reach the max time steps
   # or one the sides loses all there troops
   while (time_step <= max_steps) and (current_point[0] >= 0) and (current_point[1] >=0):
       point_list.append(tuple(current_point))
       # move to the next point in the system
       current_point = current_point + F(current_point, advantage)
       time_step = time_step +1
       
   # if the value of troops drops to negative just make the last point have a 0
   if (current_point[0] <=0):
       winner = "Blue"
       point_list.append((0, current_point[1]))
   elif (current_point[1] <= 0):
       winner = "Red"
       point_list.append((current_point[0], 0))
   
   # return the winner and the sequenc of point
   return winner, point_list # return the sequence of points (as a list of tuples)

#----------------------------------------------------------------------
    
def scatter_plot(points, advantage=1.5):
    # get the x and y values for the points
    x1 = [p[0] for p in points]
    x2 = [p[1] for p in points]
    
    
    plot_color = "red" # color the plot red
    if (x1[-1] <= 0): # if blue wins
        plot_color = "blue"
    
    plt.figure()    
    plt.plot(x1,x2, linestyle ="--", color=plot_color, marker='o', markersize=8)
    #ScatterPlot also works:  plt.scatter(x,y, alpha= 0.5, s =400)
    
    # set the bounds for the x and y axis to start at 0
    # the +0.1 gives us a bit of wiggle room before we hit the edge
    plt.ylim(0,x2[0]+0.1) 
    plt.xlim(0,x1[0]+0.1)
    
    # label the axes and title the plot    
    plt.xlabel("x1 (red)")
    plt.ylabel("x2 (blue)")
    plt.title("Start " + str(points[0]) + " Blue Adv. = " + str(advantage))
    
    # show the plot
    plt.show()
    
#===========================START===============================
    
# for different possible blue advantage avalue
for blue_adv in [1.0, 1.5, 2.0, 3.0, 5.0, 6.0]:
    # simulate the battle
    winner, points = simulate_battle(advantage=blue_adv)
    # the last point will have the final number of troops on each side
    final_troops = points[-1]
    # display the battle statisitics
    print(" \n\n The winner is", winner)
    print(" Final number of RED divisions", final_troops[0])
    print(" Final number of BLUE divisions", final_troops[1])
    print(" The battle took", len(points)-1, "hours.")
    scatter_plot(points,blue_adv)
