# print("jesus")

from typing import List

nums = [1,4,3,2,6,7,8,3,5,6,8]
nums.sort()
print(nums)
target = 11

def two_pointer(nums:list[int], target:int)->List[int]:
    l,r = 0, len(nums) -1 
    
    while l < r:
        sum = nums[l] + nums[r]
        if sum == target:
            return [l,r]
        elif sum < target:
            l +=1
        else:
            r -=1
            
    return []
print(two_pointer(nums, target)) 
    
    