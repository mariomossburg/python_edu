# two good strategies, using Sorted, or Counter. 



from collections import defaultdict
from typing import Counter, List



# x = ["eat","tea"]
# x.append([5,3])
# print(x)



# default dict? 
# def func(x: List[str])-> List[List[str]]:
#     groups = defaultdict(list)
#     print('groups: ', groups)
#     for w in x:
#         # print("w: ", w)
#         key = tuple(sorted(w)) # breaks down each word into a tuple -> 'ant' = ('a', 'n', 't')
#         # print("Key: ", key)
#         groups[key].append(w)
#     return list(groups.values())
#     # return list(groups.values())


# print(func(strs))


strs = ["eat","tea","tan","ate","nat","bat"]

def func(x: List[str])-> List[List[str]]:
    groups = defaultdict(list)
    for w in x:
        key = tuple(sorted(w))
        groups[key].append(w)
    return list(groups.values())
    
print(func(strs))
















# print(Counter(x[0]) == Counter(x[1]))
# print(Counter(x[0]))






# # my idea but bad
# def func(s: List[str])-> List[List[str]]:
#     new_list = []
#     l,r = 0, len(s) - 1

#     while l < r:
#         if Counter(s[l]) == Counter(s[r]):
#             new_list.append(s[l], s[r])
#         r-=1        
    
#     return new_list

# print(func(strs))


# strs = ["eat","tea","tan","ate","nat","bat"]

# # default dict? 
# def func(x: List[str])-> List[List[str]]:
#     groups = defaultdict(list)
#     for w in x:
#         key = tuple(sorted(w)) # breaks down each word into a tuple -> 'ant' = ('a', 'n', 't')
#         groups[key].append(w)
#     return list(groups.values())
#     # return list(groups.values())


# print(func(strs))


# def neetcode_version(x: List[str])->List[List[str]]:
#     res = defaultdict(list)
    
#     for s in x:
#         count = [0] * 26
        
#         for c in s:
#             count[ord(c) - ord('a')] +=1
        
#         res[tuple(count)].append(s)
        
#     return res.values()


