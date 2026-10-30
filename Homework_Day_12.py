# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 13:21:44 2026

@author: Riley
"""
from numpy.random import rand
import numpy as np
import matplotlib.pyplot as plt


def random_walk_2D(step_size,step_num):
    x = np.zeros((step_num,1))
    y = np.zeros((step_num,1))
    for i in range(step_num):
        flip_x = rand(1)
        if flip_x<0.5:
            x[i] = x[i-1]-step_size
        else:
            x[i] = x[i-1]+step_size
        flip_y = rand(1)
        if flip_y<0.5:
            y[i] = y[i-1]-step_size
        else:
            y[i] = y[i-1]+step_size
    plt.plot(x,y)
    plt.title("Random Walk in 2D")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
    

    x_sum = 0
    y_sum = 0
    for i in range(step_num):
        x_sum+=x[i]
        y_sum+=y[i]
    avg_disp_y = y_sum/step_num
    avg_disp_x = x_sum/step_num
    print(avg_disp_x)
    print(avg_disp_y)
    
    
    
    msd_x = np.zeros((step_num,1),"float")
    msd_y = np.zeros((step_num,1),"float")
    #msd = mean squared displacement <x^2>
    for i in range(step_num):
        for j in range(step_num-i):
            msd_x[i]+= (x[i+j]-x[j])**2/(step_num-i)
            msd_y[i]+= (y[i+j]-y[j])**2/(step_num-i)
    plt.plot(msd_x)
    plt.title("Mean Squared Displacement--x Direction")
    plt.ylabel("MSD")
    plt.xlabel("Step Size Averaged Over")
    plt.show()
    plt.plot(msd_y)
    plt.title("Mean Squared Displacement--y Direction")
    plt.ylabel("MSD")
    plt.xlabel("Step Size Averaged Over")
    plt.show()
            
    

#random_walk_2D(1,1000)

def langevin_1(R,total_time,dt):
    # simulates the dynamics of a neutrally buoyant 
    # Brownian particle of radius R moving through water
    # at room temperature
    m = 4*np.pi*R**3/3  #mass
    kBT = 4*10**(-14)   #thermal energy
    eta = 0.01          #viscosity
    zeta = 6*np.pi*eta*R    #drag coefficient
    c = np.sqrt(2*zeta*kBT/dt)  #magnitude of the stochastic force 
    #variance is c^2
    steps = round(total_time/dt)
    x = np.zeros((2,steps)) #2D motion so 2 dimensions
    v = np.zeros((2,steps))
    # start at origin with no velocity
    # equation for 1D v so we can get accurate solution w/ midpoint rule
    for i in range(1,steps):
        x_i = c*np.random.randn(2) #pluck out two random numbers
        v[:,i] = ((1-zeta*dt/2/m)*v[:,i-1]+dt*x_i/m)/(1-zeta*dt/2/m)
        v_mid = 0.5*(v[:,i] + v[:,i-1])
        x[:,i] = x[:,i-1]+dt*v_mid
        
        
    msd_x = np.zeros((10000,1),"float")
    msd_y = np.zeros((10000,1),"float")
    #msd = mean squared displacement <x^2>
    x_axis = []
    for i in range(10000):
        for j in range(10000-i):
            msd_x[i]+= (x[0][i+j]-x[0][j])**2/(steps-i)
            msd_y[i]+= (x[1][i+j]-x[1][j])**2/(steps-i)
        pick_x = (i)*dt
        x_axis.append(pick_x)
            
            
    plt.plot(x_axis,msd_x)
    plt.title("Mean Squared Displacement--x Direction")
    plt.ylabel("MSD")
    plt.xlabel("Step Size Averaged Over")
    plt.show()
    
    plt.plot(x_axis,msd_y)
    plt.title("Mean Squared Displacement--y Direction")
    plt.ylabel("MSD")
    plt.xlabel("Step Size Averaged Over")
    plt.show()
    
    plt.plot(x[0,:],x[1,:])
    plt.title("Path from Langevin Du")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
    
    x_sum = 0
    y_sum = 0
    for i in range(steps):
        x_sum+=x[0][i]
        y_sum+=x[1][i]
    avg_disp_y = y_sum/steps
    avg_disp_x = x_sum/steps
    print(avg_disp_x)
    print(avg_disp_y)
    
    

langevin_1(2e-6,0.001,1e-9)













