
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

nums = [4, 5, 1, 2, 1, 4, 5, 7] 

def func(arr:list)->dict:
    # non_repeat = None
    prevmap = {}

    for i in arr:
        if i not in prevmap:
            prevmap[i] = 1
        elif i in prevmap:
            prevmap[i] +=1


    for i in arr:
        if prevmap[i] == 1:
            return i



    return None

print(func(nums))











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




names_and_foods = [
    "Alice, Pizza",
    "Bob, Sushi",
    "Alice, Sushi",
    "Charlie, Pizza",
    "Bob, Pasta"
]


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




hashmap = {'language': 'python', 'computer': 'apple', 'gpu': 'nvidia', 'cpu': 'amd'}

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


















