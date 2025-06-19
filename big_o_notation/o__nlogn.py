# The runtime of the algorithm grows linearly with the input size and the logarithm of the input size. For example, 
# sorting an array is O(nlogn) because it takes n operations to sort the array and logn operations to sort each element.


# merge sort, quick sort

# HeapSort
import heapq
nums = [1, 2, 3, 4, 5]
heapq.heapify(nums)     # O(n)
while nums:
    heapq.heappop(nums) # O(logn)

# MergeSort (and most built-in sorting functions)



# O((log n)^2) Log squared
# for advanced algorithms like tree balancing