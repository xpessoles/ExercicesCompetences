#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""11_PompePistonAxial.py"""

__author__ = "Xavier Pessoles"
__email__ = "xpessoles.ptsi@free.fr"

import numpy as np
import matplotlib.pyplot as plt
import math as m
from scipy.optimize import newton
from scipy.optimize import fsolve

R = 0.02 # m
e = 0.01 # m

def calc_lambda(theta):
    res= e*np.sin(theta)+R
    
    return res

def calc_lambdap(theta,w):
   
    res = e*w*np.cos(theta)
    return res

def plot_debit():
    plt.cla()
    w = 100 # rad/s 
    les_t = np.linspace(0,0.1,1000)
    les_theta = w*les_t
    global e 
    S = 1e-4
    e = 20e-3
    les_q = e*S*w*np.cos(les_theta)
    plt.plot(les_t,les_q)
    plt.xlabel("Temps (s)")
    plt.ylabel("Débit (${m}^3s^{-1}$)")
    plt.grid()
    plt.savefig("11_02_c.png")
    plt.show()
    
plot_debit()