
# This section covers pages 50-58

# we can give slicing naming convention
# skip_every_other = slice(0,None,2)
# l = [10,20,30,40,50,60]
# print(l[skip_every_other])  



# my_list = [[]] * 3 # I create a lists of 3 nested lists 
# print(my_list)

# board = [['_'] * 3 for i in range(3)]
# board[1][2] = "x"


# row represents each row in the board each list 
# is represented as an index in the 2d array
# we would need a nested for loop to retreive an 
# index within a list of the lists
# for row in board:
#     print(row)
    
    
# for row in board:
#     for i in row:
#         print(i)



# car = [[] * 3 for i in range(3)]

# print(car)


# x = "hi"
# y = x
# y ="!"
# print(y)
# print(x)



#Copying an array(list) is a shared reference,,, or mutable
#when a variable is changed in one of them, it effects values for all set 
#variables
# a_list = [1,2,3]
# b_list = a_list
# b_list.append(4)
# print(a_list) # 1,2,3,4
# #instead you make a shallow copy
# c_list = b_list[:]   ......
# c_list.append(5)
# print(b_list) # prints up to 4
# print(c_list) # prints 5



# a = 5
# a*=5
# print(a)

# pythons garbage collector cleans up unreferenced objects for you
#unlike c where manual memallocation is required.a reason why it is faster.
# import sys
# a = []
# b = a
# print(sys.getrefcount(a))



#corner use case that doesn't run here, but effects
#the immutable tuple by adding to the mutable list 
# while also throwing an error. doens't print for current version of python
# t = (1,2,[30, 40])
# t[2] += [50,60] 
# print(t)




# import sys
# a = [9,7,3,6,1,2,3]
# b = a
# a.sort()
# print(a)
# print(sys.getrefcount(a))


# using built in sort
# fruits = ['grape', 'rasberry', 'apple', 'banana']
# print(sorted(fruits)) # maintains 
# print(fruits)
# print("reverse", sorted(fruits, reverse=True)) # maintains 
# print("by len", sorted(fruits, key=len)) # maintains 
# fruits.sort() # does not preserve original 
# print(fruits)




# TODO: ARRAYS
#they are not of fixed size unless enforced
import array
import sys
from typing import List

an_array = array.array('i', [1,2,3,4])
# but to make a fix size
im_fixed = array.array('i', [0] * 10000)
# print(im_fixed)
# print(an_array)
a_list = [0] * 10000

# more relevant for larger datasets
print('list in bytes:', sys.getsizeof(a_list))
print('array in bytes:', sys.getsizeof(im_fixed))

# a list doesn't enforce the type, you can use type hints with
# from typing import List
type_hint: List[int] = []
type_hint.append(1)
