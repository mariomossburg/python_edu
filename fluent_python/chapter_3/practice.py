

nums = [1,4,18,54,39,22]
target = 76



def func(nums:list[int], target:int)->list[int]:
    prevMap = {}
    
    for index, value in enumerate(nums):
        difference = target - value
        if difference in prevMap:
            return [prevMap[difference], index]
        prevMap[value] = index
    
    return[]


print(func(nums, target))






    
    
# def func(nums:list[int], target:int)->list[int]:
#     prevMap = {}

#     for i, v in enumerate(nums):
#         diff = target - v
#         if diff in prevMap:
#             print(prevMap[v], i)
#             return [prevMap[diff], i]
#         prevMap[v] = i
#     return []


# print(func(nums, target))


