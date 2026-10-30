# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 12:09:29 2026
also for Mon Sep 28 class

@author: Riley
"""

#masses m_1 and m_2 (user defined)
#coupling constant g
#decay length lambda
#total time (user defined)
#dt (user defined)
#skip (user defined)

g = 1 #coupling constant
lam = 0.5 #decay length

import matplotlib.pyplot as plt 
from matplotlib.animation import FFMpegWriter
import numpy as np

def yukawa_orbit(m_1, m_2, total_time, dt, skip):
    metadata = dict(title='YukawaOrbit', artist='Matplotlib')
    writer = FFMpegWriter(fps=15,metadata= metadata)
    fig1 = plt.figure()
    l1, = plt.plot([], [],'bo')
    l2, = plt.plot([], [],'ro')
    plt.xlim(-1, 1)
    plt.ylim(-1,1)

    #computes the dynamics of two particles of masses
    #m_1 and m_2 interacting with a Yukawa potential
    m_u = m_1*m_2/(m_1+m_2) #reduced mass
    steps = round(total_time/dt/skip) #which timesteps to save
    #need to initialize positions r_1 and r_2, velocities v_1 and v_2
    #and intiliaze times 
    #b/c conservation of angular momentum and no torque, particles stay 
    #in the same plane, so 3D problem becomes 2D (still want to track positions independently)
    r_1 = np.zeros((steps, 2), "float")
    r_2 = np.zeros((steps,2), "float")
    v_1 = np.zeros((steps,2), "float")
    v_2 = np.zeros((steps,2), "float")
    #want the initial values of r_1 and r_2 so that the center of mass is
    #at zero with a distance of 1 between the two masses
    #i.e. radius is an equilibrium condition so derivative is zero
    #define relative coordinates in plane as x,y
    times = np.zeros((steps,1),"float")
    r_1[0,0] = m_2/(m_1+m_2) #y values already zero so only need to define x
    r_2[0,0] = -m_1/(m_1+m_2)
    v_1[0,1] = np.sqrt(3*m_u*np.exp(-0.5)/2)/m_1 #velocity perpendicular to position bc ciruclar orbit
    v_2[0,1] = -np.sqrt(3*m_u*np.exp(-0.5)/2)/m_2 #-0.5 exponent comes from our definition of lamda and g
    #bound motion so total energy of this system must be negative
    #make separate arrays to temporarily store positions at each half timestep
    r_1_mid = np.zeros((1,2),"float")
    r_2_mid = np.zeros((1,2),"float")
    v_1_mid = np.zeros((1,2),"float")
    v_2_mid = np.zeros((1,2),"float")
    #initilaize done, start iteration routine
    with writer.saving(fig1,"YukawaOrbit.mp4", 100):
        for i in range(1,steps):
            r_1[i,:] = r_1[i-1,:]
            v_1[i,:] = v_1[i-1,:]
            r_2[i,:] = r_2[i-1,:]
            v_2[i,:] = v_2[i-1,:]
            
            times[i] = times[i-1] #will overwrite r, v values until next save point
            for j in range(skip):
                #compute r_1 and r_2 at half time step
                r_1_mid[0,:] = r_1[i,:]+dt*v_1[i,:]/2 #the ":" make it so we're adding column vectors
                r_2_mid[0,:] = r_2[i,:]+dt*v_2[i,:]/2 
                #now we can define the force from particle one on particle two at the midpoint
                r = np.sqrt((r_1_mid[0,0]-r_2_mid[0,0])**2 +(r_1_mid[0,1]-r_2_mid[0,1])**2) #this is calculating the dot product
                F_mag = g**2*np.exp(-lam*r)*(lam*r+1)/r**3
                
                v_1_mid[0,:] = 0.5*v_1[i,:]
                v_2_mid[0,:] = 0.5*v_2[i,:]
                
                v_1[i,:] = v_1[i,:]+dt*F_mag*(r_2_mid[0,:]-r_1_mid[0,:])/m_1
                v_2[i,:] = v_2[i,:]+dt*(-F_mag*(r_2_mid[0,:]-r_1_mid[0,:]))/m_2
                
                times[i]+=dt
                
                v_1_mid[0,:] += 0.5*v_1[i,:]
                v_2_mid[0,:] += 0.5*v_2[i,:]
                
                r_1[i,:]+=dt*v_1_mid[0,:]
                r_2[i,:]+=dt*v_2_mid[0,:]
            l1.set_data([r_1[i,0]],[r_1[i,1]])
            l2.set_data([r_2[i,0]],[r_2[i,1]])
            writer.grab_frame()
            plt.pause(0.02)
                
            
    #plt(r_1[:,0],r_1[:,1],"b",r_2[:,0],r_2[:,1],"r")
    
            
            
    
yukawa_orbit(1,2,40,0.01,40)   
    
    
    
    