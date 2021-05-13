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

R = 0.01 # m
L = 0.01 # m
w = 100
def calc_lambda(theta):
    res = R*np.cos(theta)
    res = res + np.sqrt(L*L-R*R*np.cos(theta)*np.cos(theta))
    return res

def calc_lambdap(theta,w):
    res = R*R*w*np.cos(theta)*np.sin(theta)
    res = res / np.sqrt(L*L-R*R*np.cos(theta)*np.cos(theta))
    res = res + w*R*np.cos(theta)
    return res


def calc_lambdap_bis(les_t,les_lambda):
    les_lambdap=[]
    
    for i in range(len(les_t)-1):
        les_lambdap.append((les_lambda[i+1]-les_lambda[i])/(les_t[i+1]-les_t[i]))
    
    return les_lambdap

def plot_debit():
    global L,R,w
    plt.cla()
    les_t = np.linspace(0,1,1000)
    les_theta = w*les_t
    les_lambdap = calc_lambdap(les_t,w)
    plt.plot(les_t,les_lambdap)
    plt.xlabel("Temps (s)")
    plt.ylabel("Vitesse (${m}s^{-1}$)")
    plt.grid()
    #plt.savefig("12_02_c.png")
    plt.show()
    
plot_debit()