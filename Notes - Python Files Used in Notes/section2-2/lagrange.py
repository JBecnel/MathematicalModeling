# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 11:31:13 2018

@author: becneljj
"""

import  sympy as sym  # used for symbolic mainpulation of mathematical expressions

    

  #-----------------------------------------------------------------  
    
def lagrange_algebraic(func, constraint_list, var_list = ["x1", "x2"]):
    """This function attempts to apply the method of lagrange mutlipliers 
    to maximize/minimiw the a given a particular set of constraints.
    Input: func - the function to maximize
           constraint_list - a list of function specifiying the constraints.
                         all constraints are in the form of function=0
           var_list - list of symbols sued for the independent variables in
                      character format
    Output: if a solution can be found algebraically returns the a list of
            [(variable values), max or min, (lambda values)] 
    """
    
    # create a list of the varialble symbols used in the function and the 
    # constraints
    X = [sym.symbols(x) for x in var_list]
    
    # symbolic expression for the function f
    expr_f = func(X)
    
    # create symbolic expressions for each constraint function
    constraint_expr_list = [ ]
    for g in constraint_list:
        constraint_expr_list.append(g(X))
    
    # create symbols for lambda symbols used to solve the equation
    # given by the gradient of the function = the sum of the gradients
    # of the constraint each multiplied by a different lambda
    lambda_symbols = [ ]
    for i in range(1,len(constraint_list)+1, ):
        lambda_symbols.append(sym.symbols("L" + str(i)))
    
    # for each partial derivative composing the gradient we constructed
    # an expression of the form  
    #partial of f = lambda_1*partial of constraint 1 + ....
    partial_eqs  = [ ] 
    for x in X: # for each variable
        expr = expr_f.diff(x) # find the partial of f
        # find the partial w.r.t to each constraint
        for i in range(0, len(constraint_list)):
            expr = expr - lambda_symbols[i]*constraint_expr_list[i].diff(x)
        # add the equations for each partial to the list
        partial_eqs.append(expr)
    
    #print(partial_eqs)
    # solve the partial derivative equations, finding
    # solution for each of the variables in terms of the lambda's
    solution = sym.solve(partial_eqs, X)
    
    # we now take the each constraints and subtitute the variables
    # for their solutions in terms of lambda
    # in essence all the constraints are now functions of the lambdas
    constraints_lambda = [ ]
    for expr in constraint_expr_list:
        constraints_lambda.append(expr.subs(solution))  
        
    #print(constraints_lambda)
    
    # we now solve for the lambdas using the constraint equations
    lambda_values=sym.solve(constraints_lambda,lambda_symbols, dict=True)
    #print("Lambda values", lambda_values)
    return_values=[]
    for vals in lambda_values:
        value_list = [ ]
        for x in X:
            value_list.append( solution[x].subs(vals))
        return_values.append(value_list)
        return_values.append( func(value_list))
        return_values.append(vals)    
        
    return return_values

##==============TEST CODE====================================
#
## function
#def f(X, negate=False):
#    sign = 1
#    if (negate):
#        sign = -1
#    return sign*(X[0]+2*X[1]+3*X[2])
#
## constraints
#def g(X):
#    return X[0]**2+ X[1]**2+X[2]**2-3
#
#def g2(X):
#    return X[0]-1
#
## our algrebraic solution
#solutions = lagrange_algebraic(f,[g2,g], var_list=["x","y","z"])
#print("The exact solutions:\n",solutions)
#
## numerical solution using scipy package
## constraint over which we are maximizing the function
#cons = ({'type': 'eq', # eq for equality; ineq for inequality
#         'fun' : g2},  # constraint of the form =0 or >=0
#        {'type': 'eq',
#        'fun' : g})
#bnds = ((-5,5),(-4,4),(-5,5)) # bounds for each variable
#guess = [2,1,1]  # initial guess where a solution might be
#solution = opt.minimize(f, guess, args=True ,constraints=cons, bounds=bnds )
#print("\nThe solutions dictionary:")
#print(solution)
#print("\nValue of variables:", list(solution["x"]), "Max value of function",-solution["fun"])