#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 14:25:11 2022

@author: federica
"""

from timeit import default_timer as timer
import numpy as np
import matplotlib.pyplot as plt

# DFT function
#@profile
def DFT(xr, xi, N):
    Xr, Xi = [], []
    for k in range(N):
      Xr_o, Xi_o = 0, 0
      for n in range(N):
        w = - float(n) * k * 2*np.pi/N
        Xr_o += xr[n] * np.cos(w) + xi[n] * np.sin(w)
        Xi_o += xr[n] * np.sin(w) + xi[n] * np.cos(w)
      Xr.append(Xr_o)
      Xi.append(Xi_o)
    return Xr, Xi

# Optimized DFT
#@profile
def DFT_impr(x, N):
    x = np.asarray(x, dtype=float)
    n = np.arange(N)
    k = n.reshape((N,1))
    w = - n * k * 2*np.pi/N
    W = np.cos(w) - 1j * np.sin(w)
    return np.matmul(W, x)

# Fixed N to profile the code
N = 1024
x = np.ones((N,1))
xr = np.ones((N,1))
xi = np.zeros((N,1))
X = DFT(xr, xi, N)
X_opt = DFT_impr(x,N)


# Collecting time execution for different matrix sizes 
averages = []
stds = []
N = [8, 16, 32, 64, 128, 256, 512, 1024]
t = np.zeros((len(N),6))
for j in range(6):
    for i in range(len(N)):
        #xr = np.ones((N[i],1))
        #xi = np.zeros((N[i],1))
        x = np.ones((N[i],1))
        t1 = timer()
        #DFT(xr, xi, N=N[i])
        DFT_impr(x, N=N[i])
        t2 = timer()
        t[i,j] = t2 - t1
averages.append(np.average(t, axis=1))
stds.append(np.std(t, axis=1))
        
print(averages)
print(stds)

# Plot of the results
ax = plt.bar(range(len(N)),height = list(averages[0]))
plt.xticks(np.arange(0,8), ['8', '16', '32', '64', '128', '256','512','1024'])
plt.xlabel('Matrix size N')
plt.ylabel('Execution time (s)')

