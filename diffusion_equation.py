# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 12:25:15 2026

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

def diffusion(total_time, dt, skip):
    
    D = 0.1
    steps = round(total_time/dt/skip)
    N = 100
    x,dx = np.linspace(-1,1,N,retstep = "True",dtype = "float")
    time = [skip*dt*i for i in range(steps)]
    C = np.zeros((N,steps))
    C[:,0] = np.exp(-x**2/0.1**2)
    dCd2 = np.zeros(N)
    metadata = dict(title = "Diffusion", artist = "Matplotlib")
    writer = FFMpegWriter(fps=15,codec="h264", bitrate=3000,metadata=metadata)
    fig1 = plt.figure()
    data, = plt.plot([],[],'b')
    plt.xlim(x[0],x[-1])
    plt.ylim(0,1)
    
    with writer.saving(fig1,'Diffusion.mp4',100):
    # begin time stepping
        for i in range(1,steps):
            C[:,i] = C[:,i-1]
            for j in range(skip):
            # define second derivative
                dCd2[0] = 2*(C[1,i] - C[0,i])/(dx**2)
                dCd2[1:N-1] = (C[2:N,i] - 2*C[1:N-1,i] + C[:N-2,i])/(dx**2)
                dCd2[N-1] = 2*(C[N-2,i] - C[N-1,i])/(dx**2)
                # time step concentration
                C[:,i] = C[:,i] + dt*D*dCd2
        

            data.set_data(x,C[:,i])
            writer.grab_frame()
            plt.pause(0.02)
        cmap = plt.get_cmap('PiYG')
        fig2,ax2 = plt.subplots()
        im = ax2.pcolormesh(time,x,C[:N-1,:steps-1],shading='flat',cmap=cmap)
        plt.show()




diffusion(30,0.001,2)
