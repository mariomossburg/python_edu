

# ideas for solving....
# a style of looping 

from typing import List


nums = [1,2,3,4]
# output: 24, 12, 8, 6
print(sum(nums))

def func(nums: List[int])-> List[int]:
    res: List[int] = [1] * (len(nums))
    print("nums", nums)
    
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *=nums[i]
        print("prefix", prefix, " at index:", i)
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *=postfix
        postfix *= nums[i]
        print("postfix", postfix, " at index:", i)

    return res

print(func(nums))