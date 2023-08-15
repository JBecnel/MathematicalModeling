# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 07:48:13 2019

@author: becneljj
"""
import numpy as np # numerical calculations

#---------------------------------------------------------------------
def grid_search_minimum(f, xmin, xmax, ymin, ymax, delta_x =0.2, delta_y=0.2):
    """This method performs a simple grid search to locate an approximation to
    the minimum of a given function f. The search area is specificed by by
    the square region [xmin,xmax] by [ymin, ymax] points for x and y 
    are created every delta_x, delta_y.
    """
    # create the list of x and y coordinates
    X = np.arange(xmin, xmax+delta_x, delta_x)
    Y = np.arange(ymin, ymax+delta_y, delta_y)
    
    # variables to check track of the min 
    # and the point at which is occurs
    point = [xmin, ymin]
    min = f(xmin, ymin)
    
    # for each (x,y) pair
    for x in X:
        for y in Y:
            # check if current point is the current min        
            if f(x,y) < min:
                point = [x,y]
                min = f(x,y)
           
    return point[0], point[1], min

#-------------------------------------------------------------------------------
def grid_search_maximum(f, xmin, xmax, ymin, ymax, delta_x =0.2, delta_y=0.2):
    """This method performs a simple grid search to locate an approximation to
    the maximum of a given function f. The search area is specificed by by
    the square region [xmin,xmax] by [ymin, ymax] points for x and y 
    are created every delta_x, delta_y.
    """

    neg_f = lambda x,y : -f(x,y)
    x0,y0, min = grid_search_minimum(neg_f,xmin,xmax,ymin,ymax,delta_x, delta_y)
    return x0,y0, -min
    