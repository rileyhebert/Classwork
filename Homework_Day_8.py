# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 11:02:42 2026

@author: Riley
"""

import numpy as np
import matplotlib.pyplot as plt

def backwards_euler_problem(x_0,y_0,t_i,t_f,step_num,a,b):
    times = np.linspace(t_i,t_f,step_num)
    delta_t = times[1]-times[0]
    x_s = [x_0]
    y_s = [y_0]
    for i in range(1,step_num):
        x = (x_s[i-1]+delta_t*(a+x_s[i-1]**2*y_s[i-1]))/(1+delta_t)
        x_s.append(x)
        y = (y_s[i-1]+delta_t*(b-x_s[i-1]**2*y_s[i-1]))
        y_s.append(y)
    plt.plot(times,x_s,"b", label = "x")
    plt.plot(times,y_s,"r", label = "y")
    plt.xlabel("Time")
    plt.ylabel("Concentration")
    plt.title(f"Concentration vs Time, a = {a}, b = {b}")
    plt.legend()
    plt.show()
    
a = 0.5
b = 0.3
x = 0.95*(a+b)
y = 1.1*b/(a+b)**2  
x_equ = a+b
y_equ =b/(a+b)**2
'''
print(x)
print(y)
print(x_equ)
print(y_equ)   
'''  
        
#backwards_euler_problem(x,y, 0, 10, 1000,a,b)

def m_function(m,c,w):
    m_new = c*(1-m) - 10*w*m
    return m_new

def c_function(m,c,w,t,alpha):
    if t>=3 and t<=3.2:
        c_new = 5*m*(1-c)-1.25*c+alpha
    else:
        c_new = 5*m*(1-c)-1.25*c
    return c_new
    
def w_function(m,c,w):
    w_new = 0.1*(1-w)-4*m*w
    return w_new

def runge_kutta_problem(m_0,w_0,c_0,dt,total_time,alpha):
     step_num = round(total_time/dt)
     times = np.linspace(0,total_time,step_num)
     m_s = [m_0]
     w_s = [w_0]
     c_s = [c_0]
     for i in range(0,step_num-1):
        t = times[i]
        sub_m = [m_s[i]]
        sub_c = [c_s[i]]
        sub_w = [w_s[i]]
        j = 0
        k_m_s = []
        k_c_s = []
        k_w_s = []
        while j<4:
            if j<2:
                k_m = dt*m_function(sub_m[j],sub_c[j],sub_w[j])
                sub_m.append(m_s[i]+k_m/2)
                k_m_s.append(k_m)
                
                if j==0:
                    k_c = dt*c_function(sub_m[j],sub_c[j],sub_w[j],t,alpha)
                    sub_c.append(c_s[i]+k_c/2)
                    k_c_s.append(k_c)
                elif j<3:
                    k_c = dt*c_function(sub_m[j],sub_c[j],sub_w[j],t+dt/2,alpha)
                    sub_c.append(c_s[i]+k_c/2)
                    k_c_s.append(k_c)
                else:
                    k_c = dt*c_function(sub_m[j],sub_c[j],sub_w[j],t+dt,alpha)
                    sub_c.append(c_s[i]+k_c/2)
                    k_c_s.append(k_c)
                    
                
                k_w = dt*w_function(sub_m[j],sub_c[j],sub_w[j])
                sub_w.append(w_s[i]+k_w/2)
                k_w_s.append(k_w)
            else:
                k_m = dt*m_function(sub_m[j],sub_c[j],sub_w[j])
                sub_m.append(m_s[i]+k_m)
                k_m_s.append(k_m)
                
                if j==0:
                    k_c = dt*c_function(sub_m[j],sub_c[j],sub_w[j],t,alpha)
                    sub_c.append(c_s[i]+k_c)
                    k_c_s.append(k_c)
                elif j<3:
                    k_c = dt*c_function(sub_m[j],sub_c[j],sub_w[j],t+dt/2,alpha)
                    sub_c.append(c_s[i]+k_c)
                    k_c_s.append(k_c)
                else:
                    k_c = dt*c_function(sub_m[j],sub_c[j],sub_w[j],t+dt,alpha)
                    sub_c.append(c_s[i]+k_c)
                    k_c_s.append(k_c)
                    
                
                k_w = dt*w_function(sub_m[j],sub_c[j],sub_w[j])
                sub_w.append(w_s[i]+k_w)
                k_w_s.append(k_w)
            
            j+=1
        m = m_s[i]+(k_m_s[0]+2*k_m_s[1]+2*k_m_s[2]+k_m_s[3])/6
        c = c_s[i]+(k_c_s[0]+2*k_c_s[1]+2*k_c_s[2]+k_c_s[3])/6
        w = w_s[i]+(k_w_s[0]+2*k_w_s[1]+2*k_w_s[2]+k_w_s[3])/6
        m_s.append(m)
        c_s.append(c)
        w_s.append(w)
    
     plt.plot(times,m_s,"b", label = "m")
     plt.plot(times,c_s,"r", label = "c")
     plt.plot(times,w_s,"g", label = "w")
     plt.xlabel("Time")
     plt.ylabel("Value")
     plt.title(f"Value vs Time, alpha = {alpha}")
     plt.legend()
     plt.show()   
     
        
runge_kutta_problem(0.0114,0.9374,0.0090, 0.002,30,13.7)

    
    
    
    
    

