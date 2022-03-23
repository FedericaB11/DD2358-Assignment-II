#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
from timeit import default_timer as timer
from array import *
import numpy as np 
import matplotlib.pyplot as plt
from numexpr import evaluate

# DGEMM with numexpr
def DGEMM_numexpr(N):
    A = np.ones([N,N])
    B = np.ones([N,N])*2
    C = np.zeros((N,N))
    
    C_out = evaluate('sum(A3D*B3D,2)', {'A3D':A[:,None]}, {'B3D':B[None,:]})
    #for i in range(N):
     #   for j in range(N):
      #      A_tmp = A[i,:]
       #     B_tmp = B[:,j]
        #    C_tmp = evaluate("sum(A_tmp * B_tmp )")
            
         #   C[i][j] = C_tmp
    #C_truth = np.matmul(A,B)
    #diff = C_truth - C
    #print(C.shape,np.sum(diff.flatten()))
    return C_out

# Averages and standard deviations
averages = []
stds = []
N =[64, 128, 256, 512, 1024]
t = np.zeros((len(N),6))
for j in range(6):
    for i in range(len(N)):
        t1 = timer()
        DGEMM_numexpr(N=N[i])
        t2 = timer()
        t[i,j] = t2 - t1
averages.append(np.average(t, axis=1))
stds.append(np.std(t, axis=1))
        
print(averages)
print(stds)

# Plot of execution times
ax = plt.bar(range(len(N)),height = list(averages[0]))
plt.xticks(np.arange(0,5), ['64', '128', '256','512','1024'])
plt.xlabel('Matrix size N')
plt.ylabel('Execution time (s)')
