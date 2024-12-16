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



array = [0,1,0,3,12]


def move_to_end(arr:list)->list:
    non_zero_index = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero_index], arr[i] = arr[i], arr[non_zero_index]
            non_zero_index += 1
    return arr


0,1,0,3,12

0
1