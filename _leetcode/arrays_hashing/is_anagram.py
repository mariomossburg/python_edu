from typing import Counter


s = "race"
t = "racer"


# looping through and mapping both strings to dictionaries and comparing
# will need extra memory

#hashmap solution
def isAnagram(s:str, t:str)-> bool:
    if len(s) != len(t):
        return False
    
    countS, countT = {}, {}
    
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
        
    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False
        
    return True

print(isAnagram(s,t))




# simplified in python 
def is_ana_more_efficient(s:str, t:str)-> bool:
    return Counter(s) == Counter(t)

print(is_ana_more_efficient(s,t))


def third(s:str, t:str)-> bool:
    return sorted(s) == sorted(t)
    
    
    
def isAnagram_array(s:str, t:str)-> bool:
    s, t = s.lower(), t.lower()
    if len(s) != len(t):
        return False
    
    count = [0] * 26
    for a,b in zip(s,t):
        count[ord(a) - ord('a')] +=1
        count[ord(b)- ord('a')] -=1
        
    return all(c == 0 for c in count)





