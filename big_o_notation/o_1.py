"""
Constant Time Coplexity
"""


# Array... 
# push & pop is stack functionality, but with python list has stack func built-in
nums = [1, 2, 3]
nums.append(4)    # push to end
nums.pop()        # pop from end
nums[0]           # lookup
nums[1]
nums[2]


# HashMap / Set
hashMap = {}
hashMap["key"] = 10     # insert
print("key" in hashMap) # lookup
print(hashMap["key"])   # lookup
hashMap.pop("key")      # remove
