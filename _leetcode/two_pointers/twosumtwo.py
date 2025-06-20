from typing import List

# two pointer: think if value is less than, increment left by 1
#if the sum is greater than, we shrink list by the end. fast delete from end of list.



"""
Note: code clean-up also makes function more efficient and faster on leetcode tests. less variables, most efficient conditional order, etc...

"""

nums = [1,2,3,4]
target = 3

def two_sum(nums: List[int], target:int)-> List[int]:
    l, r = 0, len(nums) - 1
    # this while loop runs faster than second
    while l < r: 
        total_sum = nums[l] + nums[r]
        
        if total_sum > target:
            r-=1
        elif total_sum < target:
            l+=1
        else:
            return[l+1, r+1]
    # while l < r:
    #     if nums[l] + nums[r] == target:
    #         return [l+1, r+1]
    #     elif nums[l] + nums[r] > target:
    #         r-=1
    #     else:
    #         l+=1
    # return []

print(two_sum(nums, target))