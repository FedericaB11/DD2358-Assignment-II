#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 09:40:11 2022

@author: federica
"""

import time
from timeit import default_timer as timer
from array import *
import numpy as np 

# DGEMM with array
def DGEMM_arr(N):
    A = list(range(N))
    B = list(range(N))
    C = list(range(N))
    for i in range(N):
        A[i] = [None] * N
        B[i] = [None] * N
        C[i] = [None] * N
        for j in range(N):
            A[i][j] = 1.0
            B[i][j] = 2.0
            C[i][j] = 0.0

    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i][j] = C[i][j] + A[i][k]*B[k][j]
    return C

# Averages and standard deviations
averages = []
stds = []
N = [64, 128, 256, 512]
t = np.zeros((len(N),6))
for j in range(6):
    for i in range(len(N)):
        t1 = timer()
        DGEMM_arr(N=N[i])
        t2 = timer()
        t[i,j] = t2 - t1
averages.append(np.average(t, axis=1))
stds.append(np.std(t, axis=1))
        
print(averages)
print(stds)


