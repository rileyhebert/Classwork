# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 13:32:11 2026

@author: Riley
"""

import biot_savart_law as bsl
import matplotlib.pyplot as plt
import numpy as np


filename = "Homework_3_csv.csv"
filename_2 = "Homework_3_csv_2D.csv"

def write_to_file():
    with open(filename_2,"a") as file:
        x = 0
        for y in range(-3,4):
            for z in range(-3,4):
                x,y,z,out = bsl.main(1,1,x,y,z)
                file.write("\n"+str(y)+","+str(z)+","+str(out[1])+","+str(out[2]))
            
            
def plot_z_vs_B_z():
    with open(filename,"r") as file:
        lines = file.readlines()
        z = []
        B_z = []
        for i in range(1,11):
            row = lines[i].strip().split(',')
            z.append(row[0])
            B_z.append(row[1])
        plt.plot(z,B_z)
        plt.title("Point on z-axis vs magnitude of magnetic field")
        plt.xlabel("Z")
        plt.ylabel("Magnitude of B")
        plt.show()
            
            
def plot_quiver():
    with open(filename_2,"r") as file:
        lines = file.readlines()
        z = []#np.linspace(-3,3,1)
        y = []#np.linspace(-3,3,1)
        #Y,Z = np.meshgrid(y,z)
        B_y = []
        B_z = []
        
        for i in range(1,len(lines)):
            row = lines[i].strip().split(',')
            
            y.append(float(row[0]))
            z.append(float(row[1]))
            B_y.append(float(row[2]))
            B_z.append(float(row[3]))
        

        plt.quiver(y,z,B_y,B_z)
        plt.xlabel("y")
        plt.ylabel("z")
        plt.title("Vector Graph of Magnetic Field in YZ Plane")
        plt.show()
        


plot_quiver()      