# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 12:26:06 2026

@author: Riley
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter

D = 0.2
#v = -x

def sample_problem(total_time, dt, node_num,C_x_i, C_x_f,skip,
                   *args,**kwargs):
    steps = round(total_time/dt/skip)
    node_num = 100
    x_s,dx = np.linspace(-1,1,node_num,retstep = "True",dtype = "float")
    v_s = -x_s
    C_s = np.zeros((node_num,steps))
    C_s[0,:] = C_x_i
    C_s[-1,:] = C_x_f
    C_s[:,0] = 1
    CV = dx*np.ones(node_num)
    CV[0] = dx/2 #control volume from integrating
    CV[node_num-1] = dx/2
    advect_terms = np.zeros(node_num)
    diffuse_terms = np.zeros(node_num)
    flux_up = np.zeros(node_num-1) #positive
    flux_down = np.zeros(node_num-1) #negative
    dCd2 = np.zeros(node_num)
    
    metadata = dict(title = "Diffusion and Advection", artist = "Matplotlib")
    writer = FFMpegWriter(fps=15,codec="h264", bitrate=3000,metadata=metadata)
    fig1 = plt.figure()
    data, = plt.plot([],[],'b')
    plt.xlim(x_s[0],x_s[-1])
    plt.ylim(0,1)
    
    
    for i in range(1,node_num):
        C_s[:,i] = C_s[:,i-1]
        for j in range(skip):
            v_half = 0.5*(v_s[1:node_num]+v_s[:node_num])
            flux_up = v_half*C_s[0:node_num-1,i]
            flux_down = v_half*C_s[1:node_num,i]
            
            flux_up[v_half<0] = flux_down[v_half<0] #upwinding
            # this account for the information flow, taking nodes from right
            #if positive and from left if negative
            #putting all the correct velocities into the flux_up array
            
            advect_terms[0] = flux_up[0]/CV[0]
            advect_terms[1:-1] = 0.5*(flux_up[1:-1]-flux_up[:-2])/CV[1:-1]
            advect_terms[-1] = -flux_up[-2]/CV[-1]
            
            dCd2[0] = 2*(C_s[1,i] - C_s[0,i])/dx/CV[0]
            dCd2[1:-1] = (C_s[2:,i] - 2*C_s[1:-1,i] + C_s[:-2,i])/dx/CV[1:-1]
            dCd2[-1] = 2*(C[-2,i] - C[N-1,i])/(dx**2)
            
            
            
            
            
            