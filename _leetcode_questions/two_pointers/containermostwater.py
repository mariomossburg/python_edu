
from typing import List
height = [1,7,2,5,4,7,3,6]


def more_eff(height: List[int])->int:
    
    res = 0
    l,r = 0, len(height) - 1

    while l < r:
        area = (r-l) * min(height[l], height[r])
        res = max(res, area)
        if height[l] < height[r]:
            l +=1
        else:
            r -= 1
    return res






"""
First try, my problem was solving was how to increment pointers, and calculating area
"""
def func(heights: List[int])-> int:
    max_area = 0
    
    l,r = 0, len(heights) - 1
    dic = {}

    while l < r:
        distance = (r - l) 
        dic[distance] = min(heights[l], heights[r]) ** 2
        if dic[distance] * distance > max_area:
            max_area = max(max_area, dic[distance])
            l+=1
        else:
            r-=1
    return max_area
        
print(func(height))
