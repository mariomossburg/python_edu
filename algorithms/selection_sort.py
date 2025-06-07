arr_unordered = [1,10,7,4,22,17,7,14,3,6]


# def selection_sort(arr: list)-> list:
#     n = len(arr)

#     for i in range(n):
#         min_index = i

#         for j in range(i+1, n):
#             if arr[j] < arr[min_index]:
#                 min_index = j
        
#         arr[i], arr[min_index] = arr[min_index], arr[i]

#     return arr

# print(arr_unordered)
# print(selection_sort(arr_unordered))


def selection_sort(arr: list)-> list:
    indexing_length = range(0, len(arr) -1)
    # print(indexing_length)

    for i in indexing_length:
        min_value = i

        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_value]:
                min_value = j

        if min_value != i:
            arr[min_value], arr[i] = arr[i], arr[min_value]

    return arr 


print(arr_unordered)
print(selection_sort(arr_unordered))







