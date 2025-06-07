from typing import List

"""
Slicing [start:stop]
includes start, excludes end
"""
#delimeter with character count of string followed by #

strs = ["sun", "is", "good", "for", "you"]



def encode(x: List[str])-> str:
    res = ''
    for s in x:
        res +=str(len(s)) + "#" + s
    return res


def decode(s: str)-> List[str]:
    res, i = [], 0
    while i < len(s):
        j = i
        while s[j] != "#":  
            j+=1
        length = int(s[i:j])
        res.append(s[j + 1 : j + 1 + length])
        i = j + 1 + length
    return res





# def decode_table(s: str)-> List[str]:
#     res, i = [], 0
#     print(f"{'i':<5} {'j':<5} {'length':<7}")
#     print("-" * 40)
#     # print("string passed to decode function:", s)
#     while i < len(s):
#         j = i
#         while s[j] != "#":  
#             j+=1
#         length = int(s[i:j])
#         print("length", length)
#         print("appending", s[j + 1 : j + 1 + length])
#         res.append(s[j + 1 : j + 1 + length])
#         i = j + 1 + length
#     return res





print("------------string------------------")
print(strs)
print("------------encoded-----------------")
print(encode(strs))
print("------------decoded-----------------")
print(decode(encode(strs)))
print("-" * 36)








# from shlex import join
# this encodes but we don't know how to seperate words
# def encode(x: List[str])->str:
#     # new_str = ''
    
#     return str(''.join(x))

# print(encode(strs))