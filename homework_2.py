# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 23:42:02 2026

@author: Riley
"""
import numpy as np

l = 23
delta_x = 0.00001
steps = int(l/delta_x)
area_under = 0
x = delta_x

def integrand(x):
    out = (1-np.e**(-x))/(x+x**3)
    return out

for step in range(steps):
    area_under = area_under+integrand(x)*delta_x
    x = x+delta_x

    
print(area_under)
    