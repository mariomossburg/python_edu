# atomic means operation is indivisible. it either completes fully or not at all

from array import array
import numpy as np


# memoryview: access and manipulate the binary data of objects 
# (like array, bytes, or bytearray) without copying it — you work with the 
# same memory buffer. It's useful for performance-critical tasks like binary 
# file parsing, image processing, or interfacing with C code

# this could be relevant for real-time data feeds, 
# fast parsing(wheather simulation), Sensor/device data (e.g., from solar inverters, smart meters)
# learn more what this is, means, and how to implement

octets = array('B', range(6))
m1 = memoryview(octets)
print(m1.tolist())
m2 = m1.cast('B', [2,3])
print(m2.tolist())
m3 = m1.cast('B', [3,2])
print(m3.tolist())
m2[1,1] = 22
m3[1,1] = 33
print(octets)


# a = np.arange(12)
# print(a)
# print(type(a))
# print(a.shape)
# a.shape = 3, 4
# print(a)
# print(a[2])
# print(a[2, 1])
# print(a[:, 1])
# print(a.transpose())




# if dequeue is of fixed size and you append, 
# it will discard an item from the other end
from collections import deque

dq = deque(range(10), maxlen=10)
print(dq)
dq.rotate(3)
print(dq)
dq.rotate(-4)
print(dq)
dq.appendleft(-1) # deletes item on the right
print(dq)
dq.extend([11,22,33]) # in order when added to end
print(dq)
dq.extendleft([10,20,30,40]) # reversed when added to front, 40 first, then 30
print(dq)

