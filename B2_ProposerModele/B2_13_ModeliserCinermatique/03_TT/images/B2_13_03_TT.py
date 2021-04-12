#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""B2_13_03_TT.py: Generation de trajectoires articulaires."""

__author__ = "Xavier Pessoles"
__email__ = "xpessoles.ptsi@free.fr"

import numpy as np
import matplotlib.pyplot as plt
import math as m
R = 0.1 # m
v = 0.01 # m.s-1 

# Temps pour faire un tour 
T = 2*m.pi*R/v

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