

"""
Arrays are fast at the tail, slow in the belly.
"""
# Arrays / Lists
# append()        -> O(1) ✅ efficient for adding to the end
# insert(0, x)    -> O(n) ❌ shifts all elements; avoid mid/front inserts
# pop()           -> O(1) ✅ fast removal from the end
# pop(0)          -> O(n) ❌ shifts everything left

"""
Hash maps are magic lockers — direct access by key.
"""
# Dictionaries / Hash Tables
# get/set         -> O(1) ✅ constant-time lookup
# key not found   -> O(1) ✅ (raises KeyError unless handled)
# iteration       -> O(n) ⚠️ linear if scanning all keys/values

"""
Sets are radar scanners — fast membership checks.
"""
# Sets
# add/remove/lookup -> O(1) ✅ efficient for uniqueness and presence
# unordered         -> ⚠️ don’t use when order matters
# convert list to set for deduplication -> O(n)

"""
Deques are revolving doors — fast at both ends.
"""
# Queues / Stacks using collections.deque
# append() / pop()        -> O(1) ✅ use as stack
# appendleft() / popleft() -> O(1) ✅ use as queue
# list.pop(0)             -> O(n) ❌ avoid for queues

"""
Binary search is cutting the phone book.
"""
# Binary Search
# O(log n) ✅ halves the problem each step
# Requires sorted input

"""
Merge sort is stacking and merging papers.
"""
# Sorting
# Merge Sort, Heap Sort  -> O(n log n) ✅ efficient, stable
# Bubble/Insertion Sort  -> O(n^2) ❌ only for small data

"""
Nested loops are handshakes in a room.
"""
# Nested Loops
# one loop        -> O(n)
# two nested loops -> O(n^2) ❌ grows fast

"""
Brute force is trying every key in a giant keyring.
"""
# Brute Force
# O(2^n), O(n!) ❌ exponential time — use only for small n (e.g. backtracking)

"""
Stacks: FILO — like a stack of plates
Queues: FIFO — like a line at the bank
"""
