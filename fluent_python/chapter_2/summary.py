
"""List comprehension"""
# builds the whole list in memory at once.
# has all built in functions available, len(), etc...
# more expressions like squares can be built in

squares = [x * x for x in range(3)] # []
# print(squares)  # [0, 1, 4]
mate = [i for i in range(10)]
# print('mate', mate)
board = [['_'] * 3 for i in range(3)]
# board[1][2] = "x"
print(board)
for row in board:
    # for index in row: # of board...
    #     print(index)
    print(row)



"""Generator expression"""
# It doesn’t build the list—it gives you one item at
# a time when you ask for it (lazy). 
# uses next(), and and is wrapped in ()
# no memory used for whole list

gen = (x * x for x in range(3)) # []
# print(next(gen)) # 0
# print(next(gen)) # 1
# print(next(gen)) # 4


"""Slicing"""

# can have naming conventions
skip_every_other = slice(0,None,2)
l = [10,20,30,40,50,60]
print('slicing:', l[skip_every_other])


"""Mutable and immutable"""
# immutable: int, str, float, tuple
a = 'genie'
b = a # initially references the same 'genie' object, this is called binding
b  += 'e' # creates a new string object, called rebinding


# mutable: list, dict, set
items = [1,2,3]
box = items # shared reference pointing to the same list object in memory
# changing any reference value that points to the list object will change the underlying object.
# since they are only references. you need to make a shallow copy in order to replicate the object
shallow_copy_obj = items[:] # creates a new list object, but replicates(shallow copy) the object it is calling 


"""Python Garbage collector"""
# python cleans up unreferenced objects for you. where malloc(), free()
# in C, you manually handle memory.
import sys
c = []
d = c
# print('ref count', sys.getrefcount(a)) # 3


"""List"""
# NOTE: list is an  array of pointers → each item is a separate PyObject
# or, python is a high-level object, includes metadata like type, reference count...adds overhead



# using built in sort, uses timsort-- a blend between
# fruits = ['grape', 'rasberry', 'apple', 'banana']
# print(sorted(fruits)) # maintains 
# print(fruits)
# print("reverse", sorted(fruits, reverse=True)) # maintains 
# print("by len", sorted(fruits, key=len)) # maintains 
# fruits.sort() # does not preserve original 
# print(fruits)

from typing import List
type_hint: List[int] = []
type_hint.append(1)


"""Important on sets"""
jim = [1,2,3]
jam = [2,3]
print(jam in jim) # false. a contains ints, not a list of ints

# we cannot use set theory with lists. Example: all items of b exist in a. 
# we must cast the list to a set first, and a set can make those comparisons. 
print(set(jam).issubset(set(jam)))
jam = set()


# rotate a list
a_list = [i for i in range(10)]
print(a_list[-3:] + a_list[:-3])


"""Arrays"""
# TODO: array or numpy array is a contigous block of memory to store raw C values directly
# no python object overhead, more compact and cache friendly

import array
#not of fixed size unless enforced

an_array = array.array('i', [1,2,3,4])
# signed represents positive and negative. unsigned represents 0 and positive



im_fixed_size = array.array('i', [0] * 10000)
im_fixed_sizerr = array.array('b', [0] * 10000)
a_list = [0] * 10000 # adjusting size
print('list in bytes:', sys.getsizeof(a_list)) # 80056
print('array in bytes i:', sys.getsizeof(im_fixed_size)) # 40080
print('array in bytes b:', sys.getsizeof(im_fixed_sizerr)) # 10080

# NOTE: Creating, saving, and loading a large array of floats
# is magnitudes faster when writing to a binary file

# a = array.array(a.typecode, sorted(a))
# To keep a sorted array sorted while adding items to it, use the
# bisect.insort function.



"""bytes"""
# a byte = 8 bits
# 1 bit represents 2 states: 0 or 1
# 1 byte can represent 256 distinct values 8^2
# 0-255 in unsigned notation
#-128 to 127 for signed notation





"""Memoryview and Numpy"""
# check the file







# unpacking and destructuring? ellipsis (...) notation?

# pattern matching in python is great











# reading: Eli Bendersky’s blog post “Less copies in Python with the buffer protocol and memo‐
# ryviews” includes a short tutorial on memoryview.
#reference pg.72 for more