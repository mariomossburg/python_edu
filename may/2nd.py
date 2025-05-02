# We will take an unsorted array, sort it, then find the target with two pointers

nums = [99,21,34,67,69,2,9,12,19,4,45,42,81,74,27,93]
target = 31
an_array = []


def bubble_sort(arr:list[int])->list[int]:
    length_nums = len(arr) - 1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, length_nums):
            if arr[i] > arr[i+1]:
                sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr
    


def two_pointer(nums:list[int], target: int):
    l,r = 0, len(nums) - 1
    
    while l < r:
        if nums[l] + nums[r] == target:
            return [l,r]
        elif nums[l] + nums[r] > target:
            r -=1
        else:
            l+=1
            
new_nums = bubble_sort(nums)
print("new_nums", new_nums)

print(two_pointer(new_nums, target))
