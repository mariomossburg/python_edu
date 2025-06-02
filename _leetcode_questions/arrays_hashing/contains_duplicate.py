

from operator import contains
from typing import List

nums=[1,2,3,4,5,6,6,7]
def contains_duplicate(nums: List[int])->bool:
    return len(nums) != len(set(nums))



print(contains_duplicate(nums))