# Count how many times each element appears in a list.



nums = [1,2,3,3,4,5,6,5,1,8,1,1,1]

def frequency(nums:list[int])->dict[int, int]:
    freq = {}
    for i in nums:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] +=1
    
    return freq


print(frequency(nums))