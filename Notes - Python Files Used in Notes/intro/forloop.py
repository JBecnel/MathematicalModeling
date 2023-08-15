# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 23:13:45 2018

@author: becneljj
"""


my_list = ["Jim", "Dwight", "Stanley"]

my_set = {"Pam", "Erin"}

number_list = [1,2,3,4]

for x in number_list:
    y = x*x
    print(y)
    

for guy in my_list:
    for gal in my_set:
        print(guy, gal)