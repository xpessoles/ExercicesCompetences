#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""14_Sympact.py"""

__author__ = "Xavier Pessoles"
__email__ = "xpessoles.ptsi@free.fr"

import numpy as np
import matplotlib.pyplot as plt
import math as m
from scipy.optimize import newton
from scipy.optimize import fsolve

R = 0.03 # m
H = 0.12     # m
w = 10 # tours /min
w = 10*2*m.pi/60  # rad/s

def calc_phi(theta):
    num = R*np.sin(theta)+H
    den = R*np.cos(theta)
    return np.arctan2(num,den)

def calc_phip(theta):
    num = R*w*(R+H*np.sin(theta))
    den = R*R+H*H+2*R*H*np.sin(theta)
    return np.arctan2(num,den)

def plot_phi():
    les_t = np.linspace(0,12,1000)
    les_theta = w*les_t
    les_phi = calc_phi(les_theta)
    plt.grid()
    plt.xlabel("Temps (s)")
    plt.ylabel("Position angulaire ($rad$)")
    #plt.plot(les_t,les_theta,label=str("$\\theta$, R=")+str(R)+" mm,"+str("H=")+str(H)+" mm")
    plt.plot(les_t,les_phi,label=str("$\\varphi$, R=")+str(R)+" mm, "+str("H=")+str(H)+" mm")
    plt.legend()
    plt.show()


def plot_phip():
    les_t = np.linspace(0,12,1000)
    les_theta = w*les_t
    les_phip = calc_phip(les_theta)
    
    plt.grid()
    plt.xlabel("Temps (s)")
    plt.ylabel("Vitesse angulaire ($rad/s$)")
    #plt.plot(les_t,les_theta,label=str("$\\theta$, R=")+str(R)+" mm,"+str("H=")+str(H)+" mm")
    plt.plot(les_t,les_phip,label=str("$\\varphi$, R=")+str(R)+" mm, "+str("H=")+str(H)+" mm")
    plt.legend()
    plt.show()

for R in [0.03,0.06,0.09]:
    plot_phip()
    
def plot_lambda():
    les_theta=np.linspace(-2*np.pi,2*np.pi,1000)
    les_l = [calc_lambda(x) for x in les_theta]
    plt.grid()
    plt.xlabel("Temps (s)")
    plt.ylabel("Vitesse (${m}s^{-1}$)")
    plt.plot(les_theta,les_l,label=str("R=")+str(R)+" mm,"+str("L=")+str(L)+" mm")
    plt.legend()
    plt.show()
    

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
    #plt.cla()
    les_t = np.linspace(0,.2,2000)
    les_theta = w*les_t
    les_lambda = calc_lambda(les_theta)
    #les_lambdap = calc_lambdap(les_t,les_lambda)
    les_lambdap = calc_lambdap_bis(les_t,les_lambda)
    plt.plot(les_t[:-1],les_lambdap,label=str("R=")+str(R)+" mm,"+str("L=")+str(L)+" mm")
    plt.xlabel("Temps (s)")
    plt.ylabel("Vitesse (${m}s^{-1}$)")
    plt.grid()
    plt.legend()
    #plt.savefig("12_02_c.png")
    plt.show()

def plot_acc(): 
    global L,R,w
    #plt.cla()
    les_t = np.linspace(0,.2,2000)
    les_theta = w*les_t
    les_lambda = calc_lambda(les_theta)
    #les_lambdap = calc_lambdap(les_t,les_lambda)
    les_lambdap = calc_lambdap_bis(les_t,les_lambda)
    les_lambdapp = calc_lambdap_bis(les_t[:-1],les_lambdap)
    plt.plot(les_t[:-2],les_lambdapp,label=str("R=")+str(R)+" mm,"+str("L=")+str(L)+" mm")
    plt.xlabel("Temps (s)")
    plt.ylabel("Accélération (${m}s^{-2}$)")
    plt.grid()
    plt.legend()
    #plt.savefig("12_02_c.png")
    plt.show()


#plot_lambda()    
#plot_debit()
#plot_acc()