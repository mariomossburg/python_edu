

s = 'hello' 

def reverse_with_stack(s:str):
    stack = list(s)
    the_reverse = []
    print(stack)
    while stack:
        the_reverse.append(stack.pop())
    
    return ''.join(the_reverse)
    
    
print(reverse_with_stack(s))
    
    
    
    

# print(''.join(nums))



# Implement a Stack That Tracks the Minimum
# Add a method get_min() that returns the minimum value in the stack in constant time.


# def get_min(nums:list)->int:
#     min = nums[0]
    
#     for i in nums:
#         if min > i:
#             min = i 
#     return min

# print(get_min(nums))



nums = [55,22,21,35,87]

def get_min(nums:list[int])->int:
    min: int = nums[0]
    
    while len(nums) >= 1:
        if nums[-1] > min:
            nums.pop()
        elif nums[-1] < min:
            min = nums[-1]
            nums.pop()
    return min

print(get_min(nums))


