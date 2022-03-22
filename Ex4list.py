import time
from timeit import default_timer as timer
from array import *
import numpy as np 

# DGEMM with lists
def DGEMM_list(N):

    A = [[1.0]*N for x in range(N)]
    B = [[2.0]*N for x in range(N)]
    C = [[0.0]*N for x in range(N)]
    
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
        DGEMM_list(N=N[i])
        t2 = timer()
        t[i,j] = t2 - t1
averages.append(np.average(t, axis=1))
stds.append(np.std(t, axis=1))
        
print(averages)
print(stds)
