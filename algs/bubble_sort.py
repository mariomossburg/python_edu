# arr_unordered = [1,10,7,4,22,17,7,14,3,6]
# n = len(arr_unordered)
# print(n)


# # big o notation of O(n^2) 
# def bubble_sort(arr: list)-> list:
#     n = len(arr)

#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:  
#                 arr[j], arr[j+1] = arr[j+1], arr[j] # swap
#     return arr

# print(bubble_sort(arr_unordered))

# # big O notation of O(n)
# def bubble(arr: list)-> list:
#     index_length = len(arr) - 1
#     sorted = False # i'm called a flag

#     while not sorted:
#         sorted = True

#         for i in range(0, index_length):
#             if arr[i] > arr[i + 1]:
#                 sorted = False
#                 arr[i], arr[i+1] = arr[i+1], arr[i]
#     return arr

# print((bubble(arr_unordered)))

import random
arr = []


def create_random_array(x: list)-> list:
    for i in range(100):
        arr.append(random.randint(0,1000))
    return arr


create_random_array(arr)

print(arr[:5])






# def bs(arr:list)->list:
#     index_length = len(arr) - 1
#     sorted = False

#     while not sorted:
#         sorted = True

#         for i in range(0, index_length):
#             if arr[i] > arr[i+1]:
#                 sorted = False
#                 arr[i], arr[i+1] = arr[i+1], arr[i]

#     return arr

# print("hello")
# print(bs(unordered))





# def bubble(arr: list)-> list:
#     index_length = len(arr) - 1
#     sorted = False # i'm called a flag

#     while not sorted:
#         sorted = True

#         for i in range(0, index_length):
#             if arr[i] > arr[i + 1]:
#                 sorted = False
#                 arr[i], arr[i+1] = arr[i+1], arr[i]
#     return arr

# print((bubble(arr_unordered)))


































