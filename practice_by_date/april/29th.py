

nums = [1,4,6,8]
target = 12
def func(nums: list[int], target: int):
    l,r = 0, len(nums)-1
    
    while l < r:
        if  nums[l] + nums[r] == target:
            return True
        elif nums[l] + nums[r] < target:
            l+=1
        else:
            r-=1
    return False

print(func(nums,target))


name = "anita"


def reverse_me(name:str)->str:
    stack = []
    z = list(name)
    while z:
        stack.append(z.pop())
    
    return ''.join(stack)

print(reverse_me(name))



def a_diff_reverse(name:str)-> str:
    return name[::-1]

print(a_diff_reverse(name))