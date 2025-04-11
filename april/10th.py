# Reviewing arrays and hashing

# nums = [1,2,3,1]

# def duplicate_exist_in_array(nums:list)->bool:
#     a_set = set(nums)


#     if len(nums) == len(a_set):
#         return False
#     else:
#         return True

# print(duplicate_exist_in_array(nums))








# If you want to compare two strings, the sorted function uses timesort(merge+insertion)
# it returns a list in order
# def isAnagram(s:str, t:str)->bool:
#     print(sorted(s))
#     print(sorted(t))
#     return sorted(s) == sorted(t)



# print(isAnagram(s='listen', t='silent'))

# this returns the indices
# def two_sum(nums:list, target:int)->list:
#     seen = {}
#     for i, num in enumerate(nums):
#         diff = target - num
#         if diff in seen:
#             return [seen[diff], i]
#         seen[num] = i

# nums = [1,3,8,5,6,11]
# target = 17
# print("two sum")
# print(two_sum(nums, target))



# nums = [1,1,1,2,2,3]
# nums = [5,7,9,3,3,5,5]
# k = 2

# def most_frequent_elements(nums:list, k:int)->list:
#     dict = {}
#     new_list = []

#     for v in nums:
#         if v in dict:
#             dict[v] += 1
#         else:
#             dict[v] = 1

#     for i in dict:
#         if dict[i] >= k:
#             new_list.append(i)

#     return new_list

# print(most_frequent_elements(nums, k))

the_tuple = [("Alice", 85), ("Bob", 90), ("Alice", 95), ("Bob", 70), ("Charlie", 100)]

print(the_tuple)
def func(nums:list)->dict:
    total = {}


print(func(the_tuple))