# list = [1,2,3,4,5,6,7,8,9]

# print(list[3:] + list[:3])



# x = True

# while x:
#     print("Escriba algo bb\n")

#     i = input()
    
#     print("te amo\n")

#     if input == 'te amo mas':
#         break
    
# while not x:
#     print('true')


# nums = [1,2,3,4,5,6,7]

# print(nums[-3:] + nums[:-3])


# nums = [5,1,2,3,9]
# target = 8



# def func(arr:list, target:int)->list:
#     l,r = 0, len(arr) - 1

#     while l < r:
#         sum = arr[l] + arr[r]
#         if sum == target:
#             return (arr[l], arr[r])
#         elif sum < target:
#             l +=1
#         else:
#             r -=1

#     return None


# print(func(nums, target))


# def bubsort(arr:list)-> list:
#     n = len(arr) - 1
#     sorted = False 

#     while not sorted:
#         sorted = True
#         for i in range(0,n):
#             if arr[i] > arr[i+1]:
#                 sorted = False
#                 arr[i], arr[i+1] = arr[i+1], arr[i]

#     return arr

# print(bubsort(nums))




# def func(arr, int):
#     l, r = 0, len(arr) - 1

#     while l < r:
#         current_sum = arr[l] + arr[r]
#         if current_sum == target:
#             return(arr[l], arr[r])
#         elif current_sum < target:
#             l +=1
#         else:
#             r -=1

#     return None


# print(func(nums, target))





# def two_sum(arr, target):
#     left, right = 0, len(arr) - 1

#     while left < right:
#         current_sum = nums[left] + nums[right]
#         if current_sum == target:
#             return( nums[left], nums[right])
#         elif current_sum < target:
#             left +=1
#         else:
#             right -=1

#     return None

# print(two_sum(nums, target))





















# dict = {'a':1, 'b': 2, 'c':3, 'd':4}

# for i in dict:
#     print(dict[i], i)


# for i in dict.values():
#     print(i)

# nums = [1,2,3,4,5,6,7,8]

# print(nums[2:] + nums[:2])


# nums = [1,2,3,4,4,4,5,6,7,8,8]
# prevmap = {}
# print('-----------------------------')
# for i in nums:

#     if i not in prevmap:
#         prevmap[i] = 1
#     elif i in prevmap:
#         prevmap[i] +=1

# print(prevmap) 

# for i in prevmap:
#     if prevmap[i] > 1:
#         print(i)













# nums = [1,2,3,4]
# print(nums[-1])

# s = 'racecarb'

# def func(s:str)-> bool:
#     return s == s[::-1]


# print(func(s))












# nums = [1,2,3,4]
# sum = 0
# for i in nums:
#     sum +=i

# print(sum)


# nums = [1,2,3,4,2]

# def compare(arr:list)->bool:
#     a = set(arr)
#     return len(a) == len(arr)


# print(compare(nums))

# nums = [4, 5, 1, 2, 1, 4, 5, 7] 

# def func(arr:list)->dict:
#     # non_repeat = None
#     prevmap = {}

#     for i in arr:
#         if i not in prevmap:
#             prevmap[i] = 1
#         elif i in prevmap:
#             prevmap[i] +=1


#     for i in arr:
#         if prevmap[i] == 1:
#             return i



#     return None

# print(func(nums))











# def func(arr:list)->set:
#     a = set()
#     non_repeat = None

#     for i in arr:
#         if i not in a:
#             a.add(i)
#         elif i in a:
#             a.remove(i)

#     return a







# arr = [1,2,4,5,6]

# def func(arr:list)-> list:
#     missing_number = 0

#     for i in range(len(arr) -1):
#         if arr[i+ 1] - arr[i] != 1:
#             missing_number = arr[i] + 1


#     return missing_number

# print(func(arr))


# nums = [1, 2, 3, 4, 5, 6, 7]
# k = 3

# def func(arr:list, x: int)-> list:
#     k = k % len(arr)

#     return arr[-k:] + arr[:-k]

# print(func(nums, k))


# array = [1, 10, 3, 4, 7]

# def func(arr:list)-> int:
#     num1= -float('inf') # initializing to smallest possible value
#     num2= -float('inf')


#     for i in arr:
#         if i > num1:
#             num2 = num1
#             num1 = i
#         elif i > num2:
#                 num2 = i


#     return num1 * num2


# print(func(array))


# # find the two numbers whose product is the smallest.

# arraz = [1, 10, 3, 4, -2]

# def smallz(arr:list)-> int:
#      num1 = -float('inf')
#      num2 = float('inf')

#      for i in arr:
#           if i > num1:
#                num1= i
#           elif i < num2:
#                num2 = i
          
#      return num1*num2

# print(smallz(arraz))


# arr = [1, 2, 2, 3, 4, 4, 5]
# hashset = set()

# for i in arr:
#     hashset.add(i)

# print(hashset)


# arr = [1,2,4,5,6]
# n = 0

# for i in range(len(arr) - 2):
#     print(arr[i])
 
# arr = [1, 10, 3, 4, 7]

# def func(x: list)->list:
#     num1 = 0
#     num2 = 0

#     for i in arr:
#         if i > num1:
#             num2 = num1
#             num1 = i
#         elif i > num2:
#             num2 = i

#     return num1 * num2

# print(func(arr))



# array = [0,1,0,3,12]


# def move_to_end(arr:list)->list:
#     non_zero_index = 0

#     for i in range(len(arr)):
#         if arr[i] != 0:
#             arr[non_zero_index], arr[i] = arr[i], arr[non_zero_index]
#             non_zero_index += 1
#     return arr


# arr = [1, 2, 4, 6]

# def func(arr:list)-> list:
#      missing_nums = []
#      for i in range(len(arr) -1):
#           if arr[i + 1] - arr[i] != 1:
#                missing_nums.append(arr[i] + 1)
#      return missing_nums

# print(func(arr))


# nums = [1,2,3,4,5]
# k = 2

# def rotate_array(arr:list, k: int)->list:
    
#     k = k % len(arr)

#     return arr[-k:] + arr[:-k]

# print(rotate_array(nums, k))


# nums = [1,2,3,4,5]

# def func(arr:list)-> int:
#     low = int('-inf')
#     high = int('-inf')
    
#     return low * high

# nums = [1,2,3,4,5,1]
# def func(arr:list)->bool:

#     return len(arr) == len(set(arr))

# print(func(nums))





# nums = [44,87,109,1,65,3,8,22,97,25,36,54]

# def func(arr:list)->list:
#     n = len(arr) - 1
#     sorted = False 

#     while not sorted:
#         sorted = True
#         for i in range(n):
#             if arr[i] > arr[i+1]:
#                 sorted = False
#                 arr[i],  arr[i+1] = arr[i+1], arr[i]
#     return arr

# print(nums)
# print(func(nums))

# def func(word: str)->str:

#     for i in range(len(word) -1):
#         if word[i] != word[i+1]:
#             return word[i]
#         else:
#             return None 

# print(func(x))
# print(func(y))


# x = 'leetcode'
# y = 'aabb'

# def func(x:str)-> str:

#     num_map = {}

# # for key, value in num_map.items():
#     for i, n in enumerate(x):
#         if n not in num_map:
#             num_map[n] = 1
#         elif n in num_map:
#             num_map[n] += 1

#     print(num_map)

#     # for i, n in enumerate(num_map):
#     #     if num_map[n] == 1:
#     #         return num_map[n]
#     # return None
#     for i in x:
#         if num_map[i] == 1:
#             return i



# print(func(x))










# Find the first infrequent number in a string

# x = 'leetcode'
# output = 'l'
# y ='aabb'


# def func(x:str)-> str:
#     prev_map = {}

#     for i, n in enumerate(x):
#         if n not in prev_map:
#             prev_map[n] = 1
#         elif n in prev_map:
#             prev_map[n] +=1

#     print(prev_map)

#     for i in x:
#         if prev_map[i] == 1:
#             return i
#         else:
#             return None

# print(func(y))

# names_and_foods = [
#     "Alice, Pizza",
#     "Bob, Sushi",
#     "Alice, Sushi",
#     "Charlie, Pizza",
#     "Bob, Pasta"
# ]

# print()
# hashmap = {}

# for i in names_and_foods:
#     x, y = i.split(', ')
#     if y not in hashmap:

#         hashmap[y] = [x]
#     else:
#         hashmap[y].append(x)



# print(hashmap)










# names_and_foods = [
#     "Alice, Pizza",
#     "Bob, Sushi",
#     "Alice, Sushi",
#     "Charlie, Pizza",
#     "Bob, Pasta"
# ]



# def func(arr:list)->dict:
#     hmap = {}

#     for i in names_and_foods:
#         name, food = i.split(', ')
#         if food not in hmap:
#             hmap[food] = [name]
#         elif food in hmap:
#             hmap[food].append(name)


#     return hmap

# print(func(names_and_foods))
    

# names_and_foods = [
#     "Alice, Pizza",
#     "Bob, Sushi",
#     "Alice, Sushi",
#     "Charlie, Pizza",
#     "Bob, Pasta"
# ]

# def func(arr:list)->dict:
#     hmap = {}

#     for i in arr:
#         name, food = i.split(', ')
#         # print(name,food)
#         if food not in hmap:
#             hmap[food] = [name]
#         elif food in hmap:
#             hmap[food].append(name)

#     return hmap

# sii = func(names_and_foods)
# print(sii)




# names_and_foods = [
#     "Alice, Pizza",
#     "Bob, Sushi",
#     "Alice, Sushi",
#     "Charlie, Pizza",
#     "Bob, Pasta"
# ]


# def func(arr:list)->dict:
#     hmap  = {}

#     for i in arr:
#         name, food = i.split(', ')
#         if food not in hmap:
#             hmap[food] = set(name)
#         elif food in hmap:
#             hmap[food].add(name)

#     return hmap

# print(func(names_and_foods))



# a  = set{1,3,2,6}
# a.add(2)
# a.add(8)
# a.add(1)
# a.add(5)

# print(a)

# for i in a:
#     print(i)


# nums = [1,8,5,7,3,11,17,12,67,91]

# nums.sort(reverse=True)
# print(nums)

# def bubble_sort(arr:list)->list:
#     sorted = False 

#     while not sorted:
#         sorted = True

#         for i in range(len(arr) - 1):
#             if arr[i] > arr[i+1]:

#                 sorted = False
#                 arr[i], arr[i+1] = arr[i + 1], arr[i]
#     return arr

# print(bubble_sort(nums))




# hashmap = {'language': 'python', 'computer': 'apple', 'gpu': 'nvidia', 'cpu': 'amd'}

# for i in hashmap:
#     print(hashmap[i])



# for k, v in hashmap.items():
#     print(k, v)




# for i in hashmap:
#     print(i)

# print("-------------------------")
# print("-------------------------")
# print("-------------------------")


# for i in hashmap:
#     if i == 'language':
#         print(hashmap[i])


# class Animal:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age

    
#     def your_age(self):
#         return (f"you are {self.age} years old")
    
    
#     def your_name(self):
#         return(f"your name is {self.name}")
    
#     # does not rely on self, don't have access to class or instance
#     # atttibutes 
#     @staticmethod
#     def static_method():
#         return ('i am a MR. static')
    

# a = Animal("tee", 15)
# print(a.your_age())
# print(a.your_name())
# print(a.static_method())




# s = 'hello world'

# def reverse_string(s:str)-> str:
#     reversed_str = ""
#     for i in range(len(s) -1, -1, -1):
#         reversed_str += s[i]
#     return reversed_str


# # print(reverse_string(s))



# arr = [3,4,7,1,3,9]
# target = 7

# def two_sum(nums:list[int], target: int)-> list[int]:
#         l,r = 0, len(nums) - 1

#         while l < r:
#             if nums[l] + nums[r] == target:
#                 return [l,r]
#             elif nums[l] + nums[r] < target:
#                 l+=1
#             else:
#                 r-=1
                
#         return []

# print(two_sum(arr,target))







# car = [1,4,2,3]

# print(*(i for i in car))
from typing import List
nums = [2,5,7,9,11,15]
target = 14

def func(nums: List[int], target: int)-> List:
    l,r = 0, len(nums) - 1
    
    while l < r:
        if nums[l] + nums[r] == target:
            return [l,r]
        elif nums[l] + nums[r] < target:
            l+=1
        else:
            r-=1
    return []

print(func(nums, target))














# nums = [1,2,3,4,5,6,7,8,9]


# print(nums)

# def func():
#     l,r = 0, len(nums) - 1
#     while l < r:
#         print("l", l)
#         print("r", r)
#         l += 1
#         r -= 1
        
# print(func())



from typing import List
nums = [3,7,4,9,11,16]
target = 14


def func(nums: List[int], target: int)-> List[int]:
    l,r = 0, len(nums) - 1
    
    while l< r:
        if nums[l] + nums[r] == target:
            return [l,r]
        elif nums[l] + nums[r] < target:
            l+=1
        else:
            r-=1
    return []
# print(func(nums, target))




hashMap ={}





print('-' * 30)

def toothpick(x:int, y:int)->int:
    
    sum = x * y
    return sum


print(toothpick(5,10))


someList = [1,1,3,4,5,6,7,8,9]



def hasdup(x: List[int])->bool:
    return len(x) == len(set(x))

print(hasdup(someList))