print('hello')



nums = [84,3,9, 2,2,6,44,88,11,43,87,12,54,19]

def bubble_sort(nums:list[int])-> list[int]:
    n = len(nums) -1
    sorted = False
    while not sorted:
        sorted  = True
        for i in range(0, n):
            if nums[i] > nums[i+1]:
                sorted = False
                nums[i], nums[i+1] = nums[i+1], nums[i]
                
    return nums
print(nums)
print(bubble_sort(nums))

target = 93
def find_target(nums:list[int], target:int):
    
    
    l,r = 0, len(nums)- 1
    while l < r:
        if target == nums[l] + nums[r]:
            return l,r
        elif target > nums[l] + nums[r]:
            l+=1
        else:
            r-=1
            
sorted_array = bubble_sort(nums)
print(find_target(sorted_array, target))




#is duplicate

def func(nums:list[int])-> bool:
    for i in nums:
        print(i)
        
    print('set')
    for i in (set(nums)):
        print(i)
    return len(nums) == len(set(nums))

print(func(nums))


def reverse(nus:list[int])->list[int]:
    return nums[::-1]

print(reverse(nums))




print(nums)
def stack_prac(nums:list[int])->list[int]:
    stack = []
    while nums:
        stack.append(nums.pop())
    return stack

print(stack_prac(nums))

