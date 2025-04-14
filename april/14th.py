print("happy monday")

# 3:20
nums = [1,1,2,3,4,5,6,6]

def manual_duplication(nums:list[int])->list:
    new_list = []

    for i in nums:
        if i not in new_list:
            new_list.append(i)

 
    return new_list

print(manual_duplication(nums))



s = 'banana'
def func(s:str)->dict:
    hashMap = {}

    for i in s:
        if i in hashMap:
            hashMap[i] += 1
        else:
            hashMap[i] = 1

    return hashMap



print(func(s))

