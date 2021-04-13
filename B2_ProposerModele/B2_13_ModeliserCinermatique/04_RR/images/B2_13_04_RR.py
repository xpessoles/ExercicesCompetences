#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""B2_13_03_TT.py: Generation de trajectoires articulaires."""

__author__ = "Xavier Pessoles"
__email__ = "xpessoles.ptsi@free.fr"

import numpy as np
import matplotlib.pyplot as plt
import math as m
from scipy.optimize import newton
from scipy.optimize import fsolve

R = 0.02 # m
v = 0.01 # m.s-1 
L = 0.015 # m

x0,y0 = -0.02,0.025
xf,yf = 0.02,0.025

# Durée du parcours
T = (2*0.02)/v

def syst(var):
    theta,psi = var[0],var[1] #psi = theta+phi
    eq1 = -0.02+v*t-R*np.cos(theta)-L*np.cos(psi)
    eq2 = 0.02-R*np.sin(theta)-L*np.sin(psi)
    res=[eq1,eq2]
    return res
    
def solve_theta ():
    plt.cla()
    les_t = np.linspace(0,T,1000)
    les_theta = []
    les_psi = []
    les_phi = []
    
    sol_ini = [0,0]
    for x in les_t :
        global t
        t=x
        sol= fsolve(syst,sol_ini)
        les_theta.append(sol[0])
        les_phi.append(sol[1]-sol[0])
        sol_ini = sol
    
    plt.plot(les_t,les_theta)
    #plt.plot(les_t,les_phi)
    plt.grid()
    plt.show()
def plot_domaine():
    plt.cla()
    les_t = np.linspace(-m.pi,m.pi)
    les_x = (R+L)*np.cos(les_t)
    les_y = (R+L)*np.sin(les_t)
    plt.plot([x0,xf],[y0,yf])
    plt.plot(les_x,les_y)
    les_x = (R)*np.cos(les_t)
    les_y = (R)*np.sin(les_t)
    plt.plot([x0,xf],[y0,yf])
    plt.plot(les_x,les_y)
    plt.axis("equal")
    plt.grid()
    plt.show()
solve_theta()
#plot_domaine()
"""
les_t = np.linspace(0,T,200)
les_lambda = R*np.cos(v/R*les_t)
les_mu = R*np.sin(v/R*les_t)
plt.grid()
plt.plot(les_t,les_lambda,label="$\\lambda(t)$")
plt.plot(les_t,les_mu,label="$\\mu(t)$")
plt.xlabel("Temps ($s$)")
plt.ylabel("Position ($m$)")
plt.legend()
#plt.show()
plt.savefig("03_TT_01_c.pdf")
plt.cla()

plt.grid()
plt.axis("equal")
plt.plot(les_lambda,les_mu,label="Trajectoire de $C$")
plt.legend()
#plt.show()
plt.savefig("03_TT_02_c.pdf")
"""