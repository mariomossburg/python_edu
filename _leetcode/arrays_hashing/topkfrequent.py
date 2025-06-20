import heapq
from typing import Counter, List
"""
Bucket Sort vs heap sort 
"""
# Bucket: O(n)
# Using Heap: Time: O(n log k), Space: O(n)


# my idea... I didn't understand freq check but did counter. Bucket sort is a 2d
# array that groups based on count/frequency
nums = [1,2,2,3,3,3]
k=2

def topKFrequent(nums: List[int], k: int) -> List[int]:
    ana = Counter(nums)
    print(ana)
    return_list = []

    for x in ana:
        print("x", x)
        if x < k:
            return_list.append(nums[x])  

    return return_list

print(topKFrequent(nums, 2))



class Solution:
    
    # @staticmethod # doesn't need constructor etc, just a utility function
    @classmethod
    def top_k_frequency(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        
        for n in nums:
            count[n] = 1 + count.get(n,0) # map freq
            
        for n, c in count.items():
            freq[c].append(n) # n occurs c number of times... populating
        
        res = []
        for i in range(len(freq) - 1, 0, -1): # reverse iteration
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
                
    def pythonic_k_freq(nums: List[int], k: int)-> List[int]:
        if k == 0:
            return []
        count = Counter(nums)# O(n)
        return heapq.nlargest(k, count.keys(), key=count.get) #O(n log k)            
            
solution = Solution()
print(solution.top_k_frequency(nums, 2))

x = Solution
print('neetcode solution', x.top_k_frequency(nums, k))
print('pythonic w/ heap solution', x.pythonic_k_freq(nums, k))
# x.top_k_frequency(nums, k=2)
            


