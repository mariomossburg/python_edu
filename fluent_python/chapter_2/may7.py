# For Cache

print('hello')

# dequeue --> double ended queue: doubly linked list under the hood
# For fifo and lifo

from collections import deque
dq = deque([1,2,3,4,5,6,7])
dq.appendleft(5)
print(dq)

# remember*** linked list has a reference pointer to the next node
# [1 | → ] → [2 | → ] → [3 | None]
# a doubly has two reference pointer, to previous and next node
# None ← [1 | ↔ ] ←→ [2 | ↔ ] ←→ [3 | → None]






# when a list is not the answer
# arrays saves a lot of memory when you need to handle millions of floating-point values
#if you are constantly adding and removing from opposite ends deque is a more efficient FIFO

from array import array
a = array('d', [1.0, 2.0, 3.0])  # compact float array...  uses far less RAM than a list of floats.


# NOTE: Creating, saving, and loading a large array of floats
# is magnitudes faster when writing to a binary file


listie = [1,2,3,4,5]
listietwo = [6,7,8,9]
listie.extend(listietwo) 
print(listie)
print(listietwo in listie) # false, however,


l = [1,2,3,4,5]
lt = [6,7,8,9]
# l.append(lt) # type: ignore # type error because lt is not of type int, is a list
# l.extend(lt) # lt in l is false, because it compares the list object, not values within
# if you type ignore and append entire list inside list(now nested) lt in l returns true


# a = array.array(a.typecode, sorted(a))
# To keep a sorted array sorted while adding items to it, use the
# bisect.insort function.





# rotate a list
a_list = [i for i in range(10)]
print(a_list[-3:] + a_list[:-3])


