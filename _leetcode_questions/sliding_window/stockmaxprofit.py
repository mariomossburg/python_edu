from typing import List
"""
Sliding window where if profitable, flip profit and max(max_profit, profit)
"""

nums = [1,2,5,4,7,1,9,7,3]


def func(l: List[int])->int: 
    l,r = 0,1
    maxprofit = 0
    while r < len(l):
        if l[l] < l[r]:
            profit = l[r] - l[l]
            maxprofit = max(maxprofit, profit)
        else:
            l = r
        r+=1
    return maxprofit
                
print(func(nums))



# def func(p: List[int])-> int:
#     l, r = 0, 1 # left buy, right sell
#     max_profit = 0
#     while r < len(p):
#         if p[l] < p[r]:
#             profit = p[r] - p[l]
#             max_profit = max(max_profit, profit)
#         else:
#             l = r
#         r+=1
         
#     return max_profit
