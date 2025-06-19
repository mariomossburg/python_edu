"""
Quadratic Time Coplexity
"""

"""
Listed O(n^2), O(m*n), O(n^3)
"""

# Traverse a square grid
nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(nums)):
    for j in range(len(nums[i])): 
        print(nums[i][j])


# Get every pair of elements in array
nums = [1, 2, 3]
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        print(nums[i], nums[j])

# Insertion sort (insert in middle n times -> n^2)





... 


# O(n * m)
# Get every pair of elements from two arrays
nums1, nums2 = [1, 2, 3], [4, 5]
for i in range(len(nums1)):
    for j in range(len(nums2)):
        print(nums1[i], nums2[j])

# Traverse rectangle grid
nums = [[1, 2, 3], [4, 5, 6]]
for i in range(len(nums)):
    for j in range(len(nums[i])):
        print(nums[i][j])
