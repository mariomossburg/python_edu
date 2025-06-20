print("Longest substring babieee")


# Given a string s, find the length of the longest substring without duplicate characters.
# A substring is a contiguous sequence of characters within a string.
Input: si = "zxyzxyz"
# Output: 3


def func(s: str)->int:
    charSet = set()
    l = 0
    res = 0
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l +=1
        charSet.add(s[r])
        res = max(res, r-l + 1)
    return res
        














# first attempt
# def func(s: str)->int:
#     max_seq = 0
#     st = set()
    
    
#     l,r = 0,1

#     while r < len(l):
#         st.add(s[l])
#         if s[l] != s[r]:
#             st.add([s[r]])
#             r+=1
#             while s[r] not in st: 
#                 st.add([s[r]])
#                 r+=1
#                 if s[r] in st:
                    
                    

                
                
            
        
        
    
    return max_seq




# questions... why if r is < len(l)