# a searching alg that repeatedly divides itself 
# in half using O(logn)

# best when applying for sorting data structures

list = [3,11,23,54,75,34,97,87,33,27,9,15]

def bs(arr, low, high, x):

    while low <= high:

        #       3      97 - 3 // 2
        # this line is mathmatically equivelent to 
        # omitting the first low, however, this correctly 
        # positions the midpoint relative to the string index
        # or accounts for index offset
        mid = low + (high - low) // 2

        if arr[mid] == x:
            return mid
        
        elif arr[mid] < x:
            low = mid + 1

        else:
            high = mid - 1
    return -1
