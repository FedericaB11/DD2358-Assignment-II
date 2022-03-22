#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 15:43:07 2022

@author: federica
"""

import time
from timeit import default_timer as timer
from array import *
import numpy as np 
import matplotlib.pyplot as plt

# DGEMM with NumPy arrays
def DGEMM_nump_arr(N):
    A = np.ones((N,N))
    B = np.ones((N,N))*2
    C = np.zeros((N,N))
    C = np.matmul(A, B.T) + C
    return C

# Averages and standard deviations
averages = []
stds = []
N = [64, 128, 256, 512, 1024, 2048]
t = np.zeros((len(N),6))
for j in range(6):
    for i in range(len(N)):
        t1 = timer()
        DGEMM_nump_arr(N=N[i])
        t2 = timer()
        t[i,j] = t2 - t1
averages.append(np.average(t, axis=1))
stds.append(np.std(t, axis=1))
        
print(averages)
print(stds)
