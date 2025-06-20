print("-----leetcode: Longest consecutive-----")

from typing import Counter, List

from numpy import sort
from sympy import Permanent

nums  = [2,5,77,3,14,4,6,98,65,34,7]

# use a set and check neighbors instead,,, more efficient!
def longconsec(nums:List[int])-> int:
    numset = set(nums)
    longest = 0
    for n in nums:
        if(n-1) not in numset:
            length = 0
            while (n + length) in numset:
                length+=1
            longest = max(length, longest)
    return longest

print(longconsec(nums))

# new_nums = Counter(nums)
# print(new_nums)

# list.sort() -- in place and Permanent
# sorted(list) not in place, not permanent

# def func(nums: List[int])-> int:
#     nums.sort()   
#     count = 0
    
#     # -1 so we don't go out of bounds when accessing nums[i+1]
#     for i in range(len(nums) - 1):
#         if nums[i+1] - nums[i] == 1:
#             count+=1

#     return count + 1
# # print(sort(list))
# print(func(nums)) 