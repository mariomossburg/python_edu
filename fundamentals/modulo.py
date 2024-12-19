# the remainder after dividing ::: a%b=r
# so 10 % 8 = 2

# to go even further, if you are to think of how many times 
# the right number goes into the left number, the result 
# will be the remainder 
print(10%8)

# when you're modding by a number larger than itself, 
# it returns the number in full. for example 8 % 10 = 8  
print(8%10)



# modulo in use, imagine rotating a social media feeds posts

arr = [1, 2, 3, 4, 5, 6, 7]
k = 3



# we normalize, because using modulo reduces the size of k to be within the
# bounds of the length of the array, and avoids exessive rotations.  
def rotate_array(arr, k):
    # Normalize k: 
    # We reduce k to be within the bounds of the array length. 
    # If k is larger than the length of the array, rotating by k steps 
    # is the same as rotating by k % len(arr) steps.
    # This avoids unnecessary full rotations that bring the array back to its original state.
    k = k % len(arr)
    # Split and reassemble:
    # arr[-k:] gives the last k elements of the array.
    # arr[:-k] gives everything before those last k elements.
    # We then concatenate them to get the rotated array.
    # For example, with arr = [1, 2, 3, 4, 5] and k = 2:
    # - arr[-2:] gives [4, 5]
    # - arr[:-2] gives [1, 2, 3]
    # The result is [4, 5, 1, 2, 3], which is the array rotated by 2 positions to the right.
    return arr[-k:] + arr[:-k]

print(rotate_array(arr, k))