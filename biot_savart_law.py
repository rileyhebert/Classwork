# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 12:57:59 2026

@author: Riley
"""
import numpy as np
import matplotlib as plt
'''
def calc_mag_field():
    x = float(input("What is the x component of the distance vector?\n"))
    y = float(input("What is the y component of the distance vector?\n"))
    z = float(input("What is the z component of the distance vector?\n"))
    #assume R = I = 1
    B_x = 0
    B_y = 0
    B_z = 0
    delta_phi = 1*0.0174533
    
    
    for i in range(361):
        phi = i*0.0174533
        r_x = (x-np.cos(phi))
        r_y = (y - np.sin(phi))
        r_z = z
        r_mag_sqrt = (r_x**2+r_y**2+r_z**2)**1/2
        B_x = B_x + r_z*np.cos(phi)*delta_phi/r_mag_sqrt**3/(4*np.pi)
        B_y = B_y + r_z*np.sin(phi)*delta_phi/r_mag_sqrt**3/(4*np.pi)
        B_z = B_z + ((-np.sin(phi)*r_y)-np.cos(phi)*r_x)*delta_phi/r_mag_sqrt**3/(4*np.pi)
        
    print(f"The magnetic field at the point ({x},{y},{z}) is ({B_x},{B_y},{B_z}).")
        
def main():
    calc_mag_field()

main()      
    
'''
  
def trapezoidal_integral(f,x,*args,**kwargs):
    N = np.size(x)
    dx = x[1]-x[0] #assume x evenly spaced
    f_0 = f(x[0],*args,**kwargs)
    is_vector = f_0.ndim >= 1
    if is_vector:
        integral = np.zeros(f_0.shape,dtype=float)
        for i in range(N-1):
            integral += 0.5*dx*(f(x[i],*args,**kwargs)+f(x[i+1],*args,**kwargs))
            
    else:
        integral = 0
        for i in range(N-1):
            integral += 0.5*dx*(f(x[i],*args,**kwargs)+f(x[i+1],*args,**kwargs))
            
    return integral

def calc_teeny_mag_vector(phi,R,I,x,y,z):
    #mu_0 = 1
    integrand = np.array([z*np.cos(phi),z*np.sin(phi),(R-x*np.cos(phi)-y*np.sin(phi))])
    denom = ((x-R*np.cos(phi))**2+(y-R*np.sin(phi))**2+z**2)**(3/2)*4*np.pi
    integrand = np.array(integrand)/denom
    return integrand

def get_inputs():
    x = float(input("What is the x component of the distance vector?\n"))
    y = float(input("What is the y component of the distance vector?\n"))
    z = float(input("What is the z component of the distance vector?\n"))
    R = float(input("What is the radius of the loop?\n"))
    I = float(input("What is the current in the loop?\n"))
    return R,I,x,y,z


def temp_trapezoidal_integral(R, I, phi, x, y, z):
    f = calc_teeny_mag_vector(R, I, phi, x, y, z)
    N = np.size(phi)
    d_phi = phi[1]-phi[0] #assume x evenly spaced
    B_x = 0.0
    B_y = 0.0
    B_z = 0.0
    for i in range(N-1):
        B_x = B_x+0.5*d_phi*(f[0][i]+f[0][i+1])
        B_y = B_y+0.5*d_phi*(f[1][i]+f[1][i+1])
        B_z = B_z+0.5*d_phi*(f[2][i]+f[2][i+1])
            
    return B_x,B_y,B_z
            
'''            
def main():
    #R, I, x, y, z, = get_inputs()
    phi = np.linspace(0,(2*np.pi),100000)
    out = trapezoidal_integral(calc_teeny_mag_vector,phi,R,I,x,y,z)
    print(out)
    return x,y,z,out
    
       
#main()

 '''        