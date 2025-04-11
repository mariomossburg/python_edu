# # more arrays and hashing


# nums = [1,2,3,4,5,6,7,8,9,10,1]

# def reverse_list(nums:list)->list:
#     return nums[::-1]


# def func(nums:list)->list:
#     return nums[::]


# # print(reverse_list(nums))
# print(func(nums))

# def rotate_array(nums:list, k:int)->list:
#     return nums[k:] + nums[:-k] 


# print(rotate_array(nums, 5))



# def contains_dupliacate(nums:list)->bool:
#     return not len(nums) == len(set(nums))


# print(contains_dupliacate(nums))


# def func(nums:list)->int:
#     new_list = []

#     # nums.sort()
#     # for i in nums:
#     #     if nums[i+1] 

#     return new_list


# nums = [2,7,11,15]
# target = 9

# def two_sum(nums:list)->list:
#     prevMap = {}

#     for i, n in enumerate(nums):
#         diff = target - n
#         if diff in prevMap:
#             return [prevMap[diff], i]
#         prevMap[n] = i


# print(two_sum(nums))

# hashmap = {'name': 'python', 'computer': 'apple', 'gpu': 'nvidia', 'cpu': 'amd'}

# def looping_dicts(data:dict):
#     for i in data:
#         print(i)
#         print(hashmap[i])
#         # print(data.keys())
#         # print(data.values())
#     return

# print(looping_dicts(hashmap))

# nums = [7,1,5,3,6,4]

# def buy_sell(prices:list[int])->int:
#     l,r = 0,1 # left=buy, right=sell
#     max_profit = 0
#     while r < len(prices):
#         if prices[l] < prices[r]:
#             profit = prices[r] - prices[l]
#             max_profit = max(max_profit, profit)
#         else:
#             l = r
#         r += 12
#     return max_profit

# print(buy_sell(nums))



# nums = [7,1,1,1,5,5,3,6,4]
# num = set(nums)
# print(nums)
# print(num)




# def contains_duplicates(nums:list)->bool:
#     return not len(nums) == len(set(nums))

# brut force
# def contains_most_water(height:list[int])->int:
#     res = 0
#     for l in range(len(height)):
#         for r in range(l+1, len(height)):
#             area = (r-l) * min(height[l], height[r])
#             res = max(res, area)
#     return res


def contains_most_water(height:list[int])->int:
    res = 0
    l, r = 0, len(height) - 1

    while l < r:
        area = (r-l) * min(height[l], height[r])
        res = max(res, area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return res



print(contains_most_water)
