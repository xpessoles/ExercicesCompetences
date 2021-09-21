#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""B2_13_07_RR3D.py."""

__author__ = "Xavier Pessoles"
__email__ = "xpessoles.ptsi@free.fr"

import numpy as np
import matplotlib.pyplot as plt
import math as m

R = 20
r = 10 

def xc(theta,phi) :
    return R*m.cos(theta)-r*m.cos(phi)*m.sin(theta)

def yc(theta,phi) :
    return R*m.sin(theta)+r*m.cos(phi)*m.cos(theta)
    
def zc(phi):
    return r*m.sin(phi)
    
les_th = np.linspace(-m.pi,m.pi,1000)
les_phi = np.linspace(-m.pi,m.pi,1000)

les_x = []
les_y = []
les_z = []

for t in les_th:
    for p in les_phi:
        les_x.append(xc(t,p))
        les_y.append(yc(t,p))
        les_z.append(zc(p))

plt.plot(les_y,les_z)
plt.grid()
plt.axis("equal")
plt.show()
