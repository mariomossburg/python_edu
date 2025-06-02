
from curses.ascii import isalnum


s = "was it a car or a cat I saw"
a = "racecar"
not_pal = 'mario'



# Doesn't meet all use cases join and reversing with slicing
# doesn't handle use cases of which aren't alphanumerical
# def func(s:str)-> bool:
#     n = ''.join(s.lower().split())
#     return n == n[::-1]


# print(func(s))




# built in isalnum method
# def func(s:str)->bool:
#     newS = ''
#     for c in s:
#         if c.isalnum():
#             newS += c.lower()
#     return newS == newS[::-1]

# print(func(not_pal))

def is_palindrome(s:str)-> bool:
    l, r = 0, len(s) - 1
    
    while l < r:
        while l < r and not alphe_num(s[l]):
            l+=1
        while r > l and not alphe_num(s[r]):
            r-=1
        if s[l].lower() != s[r].lower():
            return False
        l,r = l+1, r-1
    return True
        
        
def alphe_num(c):
   return (ord('A') <= ord(c) <= ord('Z') or
    ord('a') <= ord(c) <= ord('z') or
    ord('0') <= ord(c) <= ord('9'))
    



