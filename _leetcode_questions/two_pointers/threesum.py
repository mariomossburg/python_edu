"""3 sum"""

from typing import List
nums = [-1,0,1,2,-1,-4]

"""
Brute Force: The range for inner loops ensures no repeats... nums[0] + nums[0] + nums[1]
"""
def bruteforce(a: List[int])->List[List[int]]:
    res = [] 
    n = len(a)
    
    
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if a[i] + a[j] + a[k] == 0:
                    triplet = sorted([a[i], a[j], a[k]])
                    if triplet not in res:
                        res.append(triplet)
    return res

# print(bruteforce(nums))


# sorting -> O(log n)
# functionality -> n^2

def threesum(nums: List[int])-> List[List[int]]:
    res = []
    nums.sort() # changes original list
    # sorted(nums) I return a new sorted list without modifying original
    
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i-1]: # i do not want to be equal to the prev number... no dups please
            continue
        
        l,r = i+1, len(nums) - 1
        while l < r:
            threesum = a + nums[l] + nums[r]
            if threesum > 0:
                r -=1
            elif threesum < 0:
                l+=1
            else:
                res.append([a, nums[l], nums[r]])
                l+=1
                while nums[l] == nums[l - 1] and l < r:
                    l +=1
    return res

print("threesum best case")
print(threesum(nums))
                    
    



                    

