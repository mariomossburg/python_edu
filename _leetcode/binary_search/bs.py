from typing import List
print("Binary Search")


def binary_search(nums: List[int], target:int)-> int:
    l,r = 0, len(nums) - 1
    
    while l <= r:
        midway = (l+r) // 2 # slight bug here note below
        if nums[midway] > target:
            r = midway - 1
        elif nums[midway] < target:
            l = midway + 1
        else:
            return midway
    return -1
             
# bug doesn't appear in python due to size, however, to avoid
# wrtie out: m = l + ((r-l) // 2)
            