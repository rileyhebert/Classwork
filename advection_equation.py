# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 12:21:27 2026

@author: Riley
"""


#need to know concentration profile at initial time
# and what happens at the boundary of container
# for putting ink gently in a container of water
# this is a second order initial value problem PDE
# need to integrate once in time and twice in space -- two intergration 
# constants in space --> two boundary conditions (for 1D in space and time)
# correspond to ends of contatiner
# the flux at the edges must be zero (Neumann boundary condition b/c
# constraint on derivative of the function)


import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter

def advection(total_time, dt, skip, L,v,N):
    
    steps = round(total_time/dt/skip)
    x,dx = np.linspace(-1,1,N,retstep = "True",dtype = "float")
    time = [skip*dt*i for i in range(steps)]
    C = np.zeros((N,steps))
    C[:,0] = 0.5*(1-np.tanh((x-L/2)/0.05))
    dCdx = np.zeros(N)
    metadata = dict(title = "Advection", artist = "Matplotlib")
    writer = FFMpegWriter(fps=15,codec="h264", bitrate=3000,metadata=metadata)
    fig1 = plt.figure()
    data, = plt.plot([],[],'b')
    plt.xlim(x[0],x[-1])
    plt.ylim(0,1)
    
    with writer.saving(fig1,'Advection.mp4',100):
    # begin time stepping
        for i in range(1,steps):
            C[:,i] = C[:,i-1]
            for j in range(skip):
                # central difference derivative not correct
                #because physics says information flows left to right
                # due to positive velocity
                #i.e. the concentration only depends on the stuff before
                # while central difference tries to depend on stuff before
                # and after 
                # hence why solution always unstable when using it
                # "upwinding" = only using backward derivative b/c of this physics
                '''
                dCdx[0] = (C[1,i]-C[N-1,i])/(2*dx)
                dCdx[1:N-1] = (C[2:N,i]-C[:N-2,i])/(2*dx)
                dCdx[N-1] = (C[0,i]-C[N-2,i])/(2*dx)
                '''
                if v>=0:
                    dCdx[0] = (C[0,i]-C[N-1,i])/dx
                    dCdx[1:N] = (C[1:N,i]-C[:N-1,i])/dx
                #else:
                 #   dCdx[:N-1] = (C[1:N,i])
                
                # time step concentration
                C[:,i] = C[:,i] + -dt*v*dCdx
        

            data.set_data(x,C[:,i])
            writer.grab_frame()
            plt.pause(0.02)
        cmap = plt.get_cmap('PiYG')
        fig2,ax2 = plt.subplots()
        im = ax2.pcolormesh(time,x,C[:N-1,:steps-1],shading='flat',cmap=cmap)
        plt.show()




v = 1
L = 2
N = 50 
total_time = 1
dt = 0.01
skip = 2

advection(total_time, dt, skip, L, v, N)