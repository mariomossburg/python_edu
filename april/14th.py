# print("happy monday")

# # 3:20
# nums = [1,1,2,3,4,5,6,6]

# def manual_duplication(nums:list[int])->list:
#     new_list = []

#     for i in nums:
#         if i not in new_list:
#             new_list.append(i)

 
#     return new_list

# print(manual_duplication(nums))



# s = 'banana'
# def func(s:str)->dict:
#     hashMap = {}

#     for i in s:
#         if i in hashMap:
#             hashMap[i] += 1
#         else:
#             hashMap[i] = 1

#     return hashMap



# print(func(s))

# Create a second array
# nums = [3,5,3,4,5,6]
# def all_unique(nums:list[int])->list:
#     dup = []
#     unique = []
#     for i in nums:
#         if i in unique:
#             unique.remove(i)
#             dup.append(i)
#         elif i not in dup:
#             unique.append(i)


#     return unique

# print(all_unique(nums))


# nums = [3,5,3,4,5,6]
# def func(nums:list[int])->int:

#     hashmap = {}

#     for i in nums:
#         if i in hashmap:
#             hashmap[i] +=1
#         else:
#             hashmap[i] = 1

#     for i in hashmap:
#         if hashmap[i] == 1:
#             return i
#     return "no unique elements exist"

# print(func(nums))


# a = [1,2,3,4]
# b = [3,4,5,6]

# def func(a:list[int], b:list[int])->list:
#     intersection = []

#     for i in a:
#         if i in b:
#             intersection.append(i)
#     return intersection

# print(func(a,b))






# #####################
# nums = [2,3,2,2,5,3]

# def func(nums:list[int])->int:
#     dict = {}
#     max_freq = 0
#     me = 0


#     for i in nums:
#         if i in dict:
#             dict[i] += 1
#         else:
#             dict[i] = 1

#     for i in dict:
#         if dict[i] > max_freq:
#             max_freq = dict[i]
#             me = i
        
#     return me

# print(func(nums))


# from collections import Counter

# def func(nums: list[int]) -> int:
#     # Use Counter to count frequencies
#     count = Counter(nums)
    
#     # Find the element with the maximum frequency
#     return max(count, key=count.get)
# #################################

# a = [1, 2, 3, 4]
# b = [2, 4]

# def difference(a:list[int], b:list[int])->list[int]:
#     not_in = []

#     for i in a:
#         if i not in b:
#             not_in.append(i)

#     return not_in

# print(difference(a,b))


# seguidores = ['mario', 'tortu', 'chile', 'lumi', 'luwi']

# n = 'agus'
# def func(nums:list[str], nombre: str):
#     yo = ''

#     for i in nums:
#         if i == nombre:
#             print(nombre, ' s una amiga tuya')

#     else:
#         print('no es una amiga tuya')



# print(func(seguidores, n))

#  Two-Pointer Practice (Beginner)
# Reverse Array In-Place

# arr = [1, 2, 3, 4, 5]

# def reverse_arr(nums:list[int])->list[int]:
#     l,r = 0, (len(nums) - 1)

#     while l < r:
#         nums[l], nums[r] = nums[r], nums[l]
#         l +=1
#         r -=1

#     return nums

# print(reverse_arr(arr))






# nums = [1,2,3,4,5,6,7,8]

# def reverse_array(nums:list[int])->list[int]:
#     l,r = 0, (len(nums) -1)
#     while l < r:
#         nums[l], nums[r] = nums[r], nums[l]
#         l +=1
#         r -=1
#     return nums

# print(reverse_array(nums))
# s = 'racezmcar'

# def is_p(s:str)->bool:
#     l,r = 0, (len(s) - 1)

#     while l < r:
#         if s[l] != s[r]:
#             return False
#         l+=1
#         r-=1
#     return True

# print(is_p(s))

nums = [1,2,3,4,6]
target = 10

def func(arr:list[int], target: int):
    l,r = 0, (len(arr) - 1)

    while l < r:
        sum = arr[l] + arr[r]
        if  sum == target:
            return l, r
        elif sum < target:
            l+=1
        else:
            r-=1
print(func(nums, target))
















# Task: Reverse the list without using .reverse() or slicing.

# Is Palindrome (String)

# Input: "level"

# Task: Return True if it reads the same backward and forward.

# Find Pair with Target Sum (Sorted Array)

# Input: arr = [1, 2, 3, 4, 6], target = 6

# Task: Return indices of two numbers that add to the target.

# Remove Duplicates In-Place (Sorted Array)

# Input: [1, 1, 2, 3, 3, 4]

# Task: Remove duplicates and return new length of array.

# Merge Two Sorted Arrays

# Input: [1, 3, 5] and [2, 4, 6]

# Task: Return merged sorted array using two pointers.