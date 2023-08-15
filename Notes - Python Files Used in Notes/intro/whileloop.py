# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 23:27:40 2018

@author: becneljj
"""

# ask for an integer from the user
n = int(input("Please enter an integer: "))

# print all the numbers that divide evenly into n
divisor = n;
while divisor > 0:
    remainder = n % divisor
    if (remainder == 0):
        print(divisor)
    divisor = divisor -1

print("That is all the divisors of ", n)