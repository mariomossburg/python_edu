# with statement is syntactic sugar for wrapping logic in try/finally blocks.
# It abstracts:
# setup (__enter__)
# execution (your block)
# teardown (__exit__), even if there's an exception



"""
Working with files
"""
# with open('file.txt') as f:
#     data = f.read()
    
# print(data)


# # ugly example
# import re
# import sys
# WORD_RE = re.compile(r'\w+')
# index = {}
# with open(sys.argv[1], encoding='utf-8') as fp:
#     for line_no, line in enumerate(fp, 1):
#         for match in WORD_RE.finditer(line):
#             word = match.group()
#             column_no = match.start() + 1
#             location = (line_no, column_no)
#             # this is ugly; coded like this to make a point
#             occurrences = index.get(word, [])
#             occurrences.append(location)
#             index[word] = occurrences
# # display in alphabetical order
# for word in sorted(index, key=str.upper):
#     print(word, index[word])
    
    
# # better example
# import re # here's for regular exxpressions-> pattern matching
# import sys # let's get access to the command line, second arg will be our file
# WORD_RE = re.compile(r'\w+') # let's match words
# index = {} # let's store word locations
# with open(sys.argv[1], encoding='utf-8') as fp: # utf-8, a char encoding standard, sys arg is our file
#     for line_no, line in enumerate(fp, 1): 
#         for match in WORD_RE.finditer(line): # find all matching
#             word = match.group() # get actual matched word
#             column_no = match.start() + 1 # find column 
#             location = (line_no, column_no) # store as line, column tuple
#             index.setdefault(word, []).append(location) # setdefault is the magic when key is missing, one loop through
#             # compared to if key not in dict: will loop through 2 times, 3 if none exist.
            
# for word in sorted(index, key=str.upper):
#     print(word, index[word])


#NOTE: IM Best!!!! 
# import collections
# import re
# import sys
# WORD_RE = re.compile(r'\w+')
# index = collections.defaultdict(list)
# with open(sys.argv[1], encoding='utf-8') as fp:
#     for line_no, line in enumerate(fp, 1):
#         for match in WORD_RE.finditer(line):
#             word = match.group()
#             column_no = match.start() + 1
#             location = (line_no, column_no)
#             index[word].append(location)
# # display in alphabetical order
# for word in sorted(index, key=str.upper):
#     print(word, index[word])
    
    
    
"""
default dictionaries
"""
    
# ... defaultdicts useful when:
# You want to group or count things dynamically without checking if the key exists.
# defaultdict solves the “missing key” problem by automatically creating a value the first time a key is accessed.
# no repetitive if key not in d: d[key] = initial_value
# use when building or populating a dict, and the key may not exist yet.

# Grouping data: like tag → posts, author → articles
# Building indexes: like word → list of locations
# Graph structures: node → [connected_nodes]
# Logging errors/warnings: log_level → list of messages

# Use defaultdict(list) when you're filling a dict of lists on the fly.


import keyword

# j={}
# a=j.get('key1',None )
# print(a)


a = [1,2,3]
b = a[:]
b.append(4)
print(a)


c = 5
d = c
d+=1
print('c', c)
print('d', d)


# import collections
# a = collections.defaultdict(list)
# a['fruit'].append('apple')
# a['fruit'].append('banana')
# a['fruit'].append('blueberry')
# a['veg'].append('carrot')
# a['veg'].append('lettuce')
# print('a', a)
# print('a', a['fruit'])

# print(a['fruit'][0]) # specifying


# dic = {}
# dic['cars'].append('toyota')
# print(dic) # keyError... must initialize key beforehand
# for regular dic, key must be initialized first. 


