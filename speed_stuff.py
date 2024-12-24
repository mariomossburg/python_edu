import cProfile
import numpy as np


def slow_function():
    total = 0
    for i in range(0, 10000):
        for j in range(0, 10000):
            total += i * j
    return total

def parallel_numpy():
    i_vals = np.arange(0,10000)
    j_vals = np.arange(0,10000)
    result = np.sum(np.outer(i_vals, j_vals))
    return result

print('-----------normal nested loop-----------------')
cProfile.run('slow_function()')


print('-----------numpy nested loop-----------------')
cProfile.run('parallel_numpy()')