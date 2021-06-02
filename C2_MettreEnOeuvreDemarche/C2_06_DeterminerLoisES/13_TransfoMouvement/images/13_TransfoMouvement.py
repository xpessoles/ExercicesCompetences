#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""13_TransfoMouvement.py"""

__author__ = "Xavier Pessoles"
__email__ = "xpessoles@lamartin.fr"

import numpy as np
import matplotlib.pyplot as plt
import math as m

R = 0.04 # m
H = 0.06     # m
D = 10e-3 # 10 mm

w = 60 # tours /min
w = w*2*m.pi/60  # rad/s

def calc_lambda(theta):
    res = R*R+H*H+2*H*R*np.sin(theta)
    
    return np.sqrt(res)

def calc_lambdap(theta):
    res = -H*R*w*np.cos(theta)*np.power(R*R+H*H+2*H*R*np.sin(theta),-0.5)
    return np.sqrt(res)

def calc_lambdap_bis(les_t,les_lambda):
    les_lambda_p = []
    for i in range(len(les_t)-1):
        les_lambda_p.append((les_lambda[i+1]-les_lambda[i])/(les_t[i+1]-les_t[i]))
        
    return les_lambda_p

def plot_lambda():
    les_t = np.linspace(0,2,1000)
    les_theta = w*les_t
    les_lambda = calc_lambda(les_theta)
    plt.grid()
    plt.xlabel("Temps (s)")
    plt.ylabel("Position linéaire du piston ($m$)")
    plt.plot(les_t,les_lambda,label=str("$\\lambda$, R=")+str(R)+" mm, "+str("H=")+str(H)+" mm")
    plt.legend()
    plt.show()

def plot_lambdap():
    les_t = np.linspace(0,2,1000)
    les_theta = w*les_t
    les_lambda = calc_lambda(les_theta)
    les_lambdap = calc_lambdap(les_theta)
    plt.grid()
    plt.xlabel("Temps (s)")
    plt.ylabel("Vitesse du piston ($m/s$)")
    #plt.plot(les_t,les_lambdap,label=str("$\dot{\\lambda}$, R=")+str(R)+" mm, "+str("H=")+str(H)+" mm")
    
    les_lambdap_bis = calc_lambdap_bis(les_t,les_lambda)
    plt.plot(les_t[:-1],les_lambdap_bis,label=str("$\dot{\\lambda}$, R=")+str(R)+" mm, "+str("H=")+str(H)+" mm")

    plt.legend()
    plt.show()
    
def plot_debit():
    les_t = np.linspace(0,2,1000)
    les_theta = w*les_t
    les_lambda = calc_lambda(les_theta)
    les_lambdap = calc_lambdap(les_theta)
    plt.grid()
    plt.xlabel("Temps (s)")
    plt.ylabel("Débit ($m^3/s$)")
    #plt.plot(les_t,les_lambdap,label=str("$\dot{\\lambda}$, R=")+str(R)+" mm, "+str("H=")+str(H)+" mm")
    
    les_lambdap_bis = calc_lambdap_bis(les_t,les_lambda)
    for i in range(len(les_lambdap_bis)):
        les_lambdap_bis[i]=les_lambdap_bis[i]*np.pi*D*D/4

    plt.plot(les_t[:-1],les_lambdap_bis,label=str("Débit ($m^3/s$), R=")+str(R)+" mm, "+str("H=")+str(H)+" mm")

    plt.legend()
    plt.show()
    
#plot_lambda()
#plot_lambdap()
plot_debit()

