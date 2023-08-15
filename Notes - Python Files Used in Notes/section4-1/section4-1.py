# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 15:10:36 2019

@author: becneljj
"""

import sympy as sym

# sysmbols used in equilibrium equations
x1, x2 = sym.symbols("x1,x2")
r1, r2 = sym.symbols("r1,r2")
a1, a2 = sym.symbols("a1,a2")
b1, b2 = sym.symbols("b1,b2")

# equilibrium equations
eq1 = r1*x1-a1*x1**2-b1*x1*x2
eq2 = r2*x2-a2*x2**2-b2*x1*x2

# find the solutions to the equation
solutions = sym.solve([eq1,eq2],[x1,x2])

# print the solutions line by lien
for s in solutions:
    print("\nA solution is:", s)
