
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


array = [1, 10, 3, 4, 7]

def func(arr:list)-> int:
    num1= -float('inf') # initializing to smallest possible value
    num2= -float('inf')

    for i in arr:
        if i > num1:
            num2 = num1
            num1 = i
        elif i > num2:
                num2 = i


    return num1 * num2


print(func(array))


# find the two numbers whose product is the smallest.

arraz = [1, 10, 3, 4, -2]

def smallz(arr:list)-> int:
     num1 = -float('inf')
     num2 = float('inf')

     for i in arr:
          if i > num1:
               num1= i
          elif i < num2:
               num2 = i
          
     return num1*num2

print(smallz(arraz))


























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





