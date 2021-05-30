#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""12_BielleManivelle.py"""

__author__ = "Xavier Pessoles"
__email__ = "xpessoles.ptsi@free.fr"

import numpy as np
import matplotlib.pyplot as plt
import math as m
from scipy.optimize import newton
from scipy.optimize import fsolve

R = 0.01 # m
L = 0.03 # m
w = 100
def calc_lambda(theta):
    #res = R*np.sin(theta)
    #print(L*L-R*R*np.cos(theta)*np.cos(theta))
    #res = res + np.sqrt(L*L-R*R*np.cos(theta)*np.cos(theta))
    res = np.sqrt(L*L-R*R*np.cos(theta)*np.cos(theta))+R*np.sin(theta)
    return res

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
    plt.ylabel("Vitesse (${m}s^{-1}$)")
    plt.grid()
    plt.legend()
    #plt.savefig("12_02_c.png")
    plt.show()


#plot_lambda()    
#plot_debit()
plot_acc()