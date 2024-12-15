arr_unordered = [1,10,7,4,22,17,7,14,3,6]

print(arr_unordered)

def insertion_sort(arr: list)-> list:

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    return arr



print(insertion_sort(arr_unordered))