# -----------When you want to use two-pointers--------------
# - **Find Triplets with Zero Sum**: Given an array, find all unique triplets that add up to zero using two pointers with the array sorted.  

# - **Maximum Water Container**: Determine the maximum amount of water a container can store using heights as boundaries, moving two pointers inward to maximize the area.  

# - **Subarray with Target Sum**: Find a contiguous subarray whose sum equals a target value, adjusting pointers as needed in a sliding window.  

# - **Longest Substring Without Repeating Characters**: Identify the length of the longest substring in a string without duplicate characters using two pointers and a hash set.  

# - **Intersection of Two Sorted Arrays**: Find the common elements in two sorted arrays using two pointers to compare elements and move forward.  


# ---------Notes on Two-Pointer Strategy and Functions-------------

# **Two-Pointer Strategy**
# an efficient algorithmic approach to solve problems involving arrays or strings. 

# It uses two indices(pointers) to traverse the data structure, often reducing the time complexity of operations like searching or modifying arrays. 

# Common variations:

# 1. Same direction: Both pointers move in tandem (e.g., sliding window problems).
# 2. Opposite direction: One pointer starts at the beginning and the other at the end (e.g., searching for a pair with a specific sum).

# **Function: remove_duplicates**
# This function removes duplicates from a sorted array in-place, ensuring each element appears only once.
# It uses two pointers ("slow" and "fast") to traverse the array and modify it:
# - `slow` tracks the position of the last unique element.
# - `fast` traverses the array to find the next unique element.
# - If a new unique element is found, it is moved to the position after `slow`.
# The function returns the length of the modified array.

def remove_duplicates(arr: list) -> int:
    if not arr:  # Handle edge case of an empty array.
        return 0
    
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:  # Check if current element is unique.
            slow += 1  # Move slow pointer to the next unique position.
            nums[slow] = nums[fast]  # Update array to include the new unique element.
    return slow + 1  # Return the length of the unique elements.

# Example usage of remove_duplicates
nums = [2, 2, 5, 3, 8, 8, 4, 6, 1, 9, 3, 7, 8, 4]
length = remove_duplicates(nums)
print(length, nums[:length])  # Output: Length of unique array and unique elements.

# **Function: two_sum**
# This function finds two numbers in a sorted array that add up to a given target value.
# It uses two pointers ("left" and "right"):
# - `left` starts at the beginning of the array.
# - `right` starts at the end of the array.
# - The pointers are adjusted based on the sum of their elements compared to the target:
#   - If the sum is less than the target, move `left` forward to increase the sum.
#   - If the sum is greater than the target, move `right` backward to decrease the sum.
# The function returns the indices of the two numbers if a pair is found; otherwise, it returns an empty list.

def two_sum(nums, target):
    left, right = 0, len(nums) - 1  # Initialize pointers.
    while left < right:
        current_sum = nums[left] + nums[right]  # Calculate current sum.
        if current_sum == target:  # Check if target is found.
            return [left, right]
        elif current_sum < target:  # Adjust pointers based on sum.
            left += 1
        else:
            right -= 1
    return []  # Return empty list if no pair is found.

# Example usage of two_sum
nums = [2, 2, 5, 3, 8, 8, 4, 6, 1, 9, 3, 7, 8, 4]  # Input array.
target = 6
print(two_sum(nums, target))  # Output: Indices of two numbers that sum up to the target.
