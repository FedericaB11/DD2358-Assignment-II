import time
from timeit import default_timer as timer
import sys
from array import *
import numpy as np
import matplotlib.pyplot as plt


# Numpy
import time
from timeit import default_timer as timer
import sys
from array import *
import numpy as np


STREAM_ARRAY_SIZE = []
for i in range(100):
    STREAM_ARRAY_SIZE.append(i**2)
    
bandwidth_copy = []
bandwidth_scale = []
bandwidth_sum = []
bandwidth_triad = []
times_bandwidth = []


#copy 
def copy_numpy(a):
    return a.copy()

#scale
def scale_numpy(c, scalar):
    return np.dot(scalar, c)
    
# sum
def sum_numpy(a, b):
    return np.add(a, b)

# triad
def triad_numpy(b, c, scalar):
    return np.add(b, np.dot(scalar, c))

for i in STREAM_ARRAY_SIZE:

    a = np.arange(i)
    b = np.arange(i)
    c = np.arange(i)
    times = list(range(4))

    a.fill(1.0)
    b.fill(2.0)
    c.fill(0.0)
    scalar = 2.0

    # copy
    times[0] = timer()
    c = copy_numpy(a)
    times[0] = timer() - times[0]

    # scale
    times[1] = timer()
    b = scale_numpy(c, scalar)
    times[1] = timer() - times[1]
    #sum
    times[2] = timer()
    c = sum_numpy(a, b)
    times[2] = timer() - times[2]

    # triad
    times[3] = timer()
    a = triad_numpy(b, c, scalar)
    times[3] = timer() - times[3]
    
    bandwidth_copy.append((2 * sys.getsizeof(a) * i)/times[0])
    bandwidth_sum.append((2 * sys.getsizeof(a) * i)/times[1])
    bandwidth_scale.append((3 * sys.getsizeof(a) * i)/times[2])
    bandwidth_triad.append((3 * sys.getsizeof(a) * i)/times[3])
    times_bandwidth.append((times))
    
#print(times_bandwidth)
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