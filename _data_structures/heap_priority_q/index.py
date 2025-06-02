# A heap is a concrete data structure—usually a complete binary tree stored in 
# an array—that enforces the heap property (e.g. in a min-heap every parent ≤ its children).
# It supports push/pop in O(log n) and heapify in O(n).

# A priority queue is an abstract data type (ADT) where each element has a priority, 
# and you always dequeue the element with the highest (or lowest) priority. Heaps are 
# the most common backing for priority queues, but you can also use balanced BSTs, 
# Fibonacci heaps, or even buckets for integer priorities.

# minheap has smallest element at top of tree, maxheap is opposite

import heapq

data = [10,20,43,1,2,65,17,44,2,3,1]
# print(data)
# print(sorted(data)) # works, but inserting new element, linear runtime, let's use a heap so not linear, but logarithmic

heapq.heapify(data) # minheap
print('heapified', data)
print(heapq.heappop(data))
print('heapified', data)

# heappop pops and heapifies. it cares about maintaining the valid heap

heapq.heappush(data, 2)


# better to implement you own DS for maxheap. !!! 
data_copy  = data[:]
heapq._heapify_max(data_copy)
print('minheap', data)
print('maxheap', data_copy)



# merge list into a heap 
l1 = [10,20,30,40,50]
l2 = [15,25,35,45,55]

l3 = heapq.merge(l1,l2)
print(list(l3))




# it's structure? 
# i
# 2*i+1 ... first chold index
#2*i+2 ... second child index
#(i-1)/2





# aaa = [i for i in range(500)]
# print('aaa', aaa)

# aaa.insert(250, 999)
# print('aaa', aaa)


