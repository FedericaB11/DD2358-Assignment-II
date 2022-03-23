#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
from timeit import default_timer as timer
import sys
from array import *
import numpy as np
import matplotlib.pyplot as plt

# List

STREAM_ARRAY_SIZE = []
for i in range(100):
    STREAM_ARRAY_SIZE.append(i**2)
    
bandwidth_copy = []
bandwidth_scale = []
bandwidth_sum = []
bandwidth_triad = []
times_bandwidth = []

for i in STREAM_ARRAY_SIZE:

    a = list(range(i))
    b = list(range(i))
    c = list(range(i))
    times = list(range(4))

    for j in range(i):
        a[j] = 1.0
        b[j] = 2.0
        c[j] = 0.0
    scalar = 2.0

    # copy
    times[0] = timer()
    for j in range(i):
        c[j] = a[j]
    times[0] = timer() - times[0]

    # scale
    times[1] = timer()
    for j in range(i):
        b[j] = scalar*c[j]
    times[1] = timer() - times[1]
    #sum
    times[2] = timer()
    for j in range(i):
        c[j] = a[j]+b[j]
    times[2] = timer() - times[2]

    # triad
    times[3] = timer()
    for j in range(i):
        a[j] = b[j]+scalar*c[j]
    times[3] = timer() - times[3]
    
    bandwidth_copy.append((2 * sys.getsizeof(a) * i)/times[0])
    bandwidth_sum.append((2 * sys.getsizeof(a) * i)/times[1])
    bandwidth_scale.append((3 * sys.getsizeof(a) * i)/times[2])
    bandwidth_triad.append((3 * sys.getsizeof(a) * i)/times[3])
    times_bandwidth.append((times))
    
print(times_bandwidth)
print(bandwidth_copy)
print(bandwidth_sum)
print(bandwidth_scale)
print(bandwidth_triad)

# Plot results
plt.plot(STREAM_ARRAY_SIZE, bandwidth_copy, 'darkorange')
plt.plot(STREAM_ARRAY_SIZE, bandwidth_sum, 'deepskyblue')
plt.plot(STREAM_ARRAY_SIZE, bandwidth_scale, 'blue')
plt.plot(STREAM_ARRAY_SIZE, bandwidth_triad, 'deeppink')
plt.xlabel('STREAM_ARRAY_SIZE')
plt.ylabel('Bandwidth')
plt.legend(['Copy', 'Sum', 'Scale', 'Triad'])
