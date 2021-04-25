#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""10_PompePalette.py"""

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
    res= e*np.cos(theta)
    res = res+np.sqrt(e*e*np.cos(theta)*np.cos(theta)-e*e+R*R)
    return res

def calc_lambdap(theta,w):
    print(e*e*np.cos(theta)*np.cos(theta)-e*e*+R*R)
    tmp = np.sqrt(e*e*np.cos(theta)*np.cos(theta)-e*e*+R*R)
    res = -e*e*w*np.cos(theta)*np.sin(theta)/tmp
    res = res -e*w*np.sin(theta)
    return res

def calc_lambdap_bis(les_t,les_lambda):
    les_lambdap=[]
    
    for i in range(len(les_t)-1):
        les_lambdap.append((les_lambda[i+1]-les_lambda[i])/(les_t[i+1]-les_t[i]))
    
    return les_lambdap
    
    
def plot_lambda():
    plt.cla()
    les_theta = np.linspace(-m.pi,m.pi,1000)
    les_lambda = calc_lambda(les_theta)
    plt.grid()
    plt.plot(np.degrees(les_theta),les_lambda)
    plt.plot(np.degrees(les_theta),les_lambda)
    plt.xlabel("$\\theta$ (deg)")
    plt.ylabel("$\\lambda(t)$ (m)")
    plt.show()
    #plt.savefig("10_02_c.pdf")

def plot_lambdap():
    plt.cla()
    w = 2*m.pi # rad/s (1tr/s)
    les_t = np.linspace(0,1.01,1000)
    les_theta = w*les_t
    les_lambda = calc_lambda(les_theta)
    les_lambdap = calc_lambdap_bis(les_t,les_lambda)
    plt.grid()
    
    
    les_t = les_t[0:-1]
    les_theta = les_theta[0:-1]
    
    
    plt.plot(np.degrees(les_theta),les_lambdap)
    
    les_lambdap=[calc_lambdap(x,w) for x in les_theta]
    #plt.plot(les_theta,les_lambdap)


    plt.xlabel("$\\theta$ (deg)")
    plt.ylabel("$\\dot{\\lambda}(t)$ (m)")
    #plt.show()
    plt.savefig("10_03_c.pdf")

def plot_debit():
    plt.cla()
    w = 2*m.pi # rad/s (1tr/s)
    les_t = np.linspace(0,1.01,1000)
    les_theta = w*les_t
    global e 
    e = 10e-3
    les_lambda = calc_lambda(les_theta)
    les_lambdap = calc_lambdap_bis(les_t,les_lambda)
    les_lambdap = np.array(les_lambdap)
    
    e = 15e-3
    les_lambda = calc_lambda(les_theta)
    les_lambdap2 = calc_lambdap_bis(les_t,les_lambda)
    les_lambdap2 = np.array(les_lambdap2)    
    
    plt.grid()
    
    les_t = les_t[0:-1]
    les_theta = les_theta[0:-1]
    
    S= 1e-4
    
    plt.plot(np.degrees(les_theta),S*les_lambdap,label="e = 10 mm")
    plt.plot(np.degrees(les_theta),S*les_lambdap2,label="e = 15 mm")
    plt.legend()
    plt.xlabel("$\\theta$ (deg)")
    plt.ylabel("Débit instantané $m^3s^{-1}$")
    #plt.show()
    plt.savefig("10_04_c.pdf")


def plot_debit5p():
    plt.cla()
    w = 2*m.pi # rad/s (1tr/s)
    les_t = np.linspace(0,6,6000)
    les_theta = w*les_t
   
    # Calcul de la vitesse instantanée des pistons.
    les_lambda = calc_lambda(les_theta)
    les_lambdap = calc_lambdap_bis(les_t,les_lambda)
    les_lambdap = np.array(les_lambdap)
    
    S= 1e-4 # Surface en m2
    
    # 5 courbes de débit décalées d'un cinquième de tour
    les_q1 = S*les_lambdap
    les_q2 = S*les_lambdap[200:]
    les_q3 = S*les_lambdap[400:]
    les_q4 = S*les_lambdap[600:]
    les_q5 = S*les_lambdap[800:]
    
    # On conserve que les valeurs que sur un tour
    les_q1 = les_q1[:1000]
    les_q2 = les_q2[:1000]
    les_q3 = les_q3[:1000]
    les_q4 = les_q4[:1000]
    les_q5 = les_q5[:1000]
    plt.grid()
    
    les_t = les_t[:1000]
    les_theta = les_theta[:1000]
  
    plt.xlabel("$\\theta$ (deg)")
    plt.ylabel("Débit instantané $m^3s^{-1}$")
    
    # On conserve que les valeurs positives (débit)
    for i in range(len(les_q1)):
        if les_q1[i]<0:
            les_q1[i]=0
        if les_q2[i]<0:
            les_q2[i]=0
        if les_q3[i]<0:
            les_q3[i]=0
        if les_q4[i]<0:
            les_q4[i]=0
        if les_q5[i]<0:
            les_q5[i]=0

    plt.plot(np.degrees(les_theta),les_q1)
    plt.plot(np.degrees(les_theta),les_q2)
    plt.plot(np.degrees(les_theta),les_q3)
    plt.plot(np.degrees(les_theta),les_q4)
    plt.plot(np.degrees(les_theta),les_q5)
    
    # Le débit instantané est la sommme des contributions
    plt.plot(np.degrees(les_theta),les_q1+les_q2+les_q3+les_q4+les_q5)
    #plt.show() 
    #plt.savefig("10_05_c.pdf")


plot_debit5p()

"""
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