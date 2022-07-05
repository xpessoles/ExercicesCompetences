# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 21:21:39 2022

@author: xpess
"""

Amax = 10**(7/20)
a = 4
b = -4 
c = 1/Amax/Amax
delta = b*b-4*a*c

X1 = (-b-delta**(0.5))/(2*a) 
X2 = (-b+delta**(0.5))/(2*a)

xi1 = X1**(0.5)
xi2 = X2**(0.5)