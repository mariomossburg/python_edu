
"""
This file documents the average and worst-case time complexities and space complexities
for key Python built-in and standard-library data structures.
"""

# 1. list (dynamic array)

# --------------------------------------------------
# Underlying: contiguous block of memory, resizable.
# Operations:
#   Access by index      O(1) time
#   Search (value in list) O(n)
#   Append               O(1) amortized (occasionally O(n) when resizing)
#   Insert/Delete at end  O(1) amortized
#   Insert/Delete at front or middle O(n) (shifts elements)
# Space: O(n) for storing n elements; extra overallocation amortizes resizing.

# 2. tuple (immutable sequence)
# --------------------------------------------------
# Underlying: contiguous, fixed-size block of memory.
# Operations:
#   Access by index      O(1)
#   Search               O(n)
#   Concatenation        O(n)
# Space: O(n) exact; no over-allocation since size fixed.

# 3. dict (hash table)
# --------------------------------------------------
# Underlying: hash table with open addressing and dynamic resizing.
# Average-case operations:
#   Lookup by key        O(1)
#   Insert                O(1)
#   Delete                O(1)
# Worst-case (e.g., many hash collisions) O(n)
# Python implements hash tables with resizing when load factor grows,
# ensuring O(1) expected complexity. Hash function: uses __hash__() + perturbation.
# Space: O(n) for entries plus overhead for table capacity (load factor ~2/3).

# 4. set (hash-based)
# --------------------------------------------------
# Underlying: similar to dict but only keys stored.
# Average-case:
#   Membership test     O(1)
#   Add/Delete          O(1)
# Worst-case           O(n)
# Space: O(n) plus overhead for capacity.

# 5. OrderedDict (collections.OrderedDict)
# --------------------------------------------------
# Underlying: doubly-linked list + hash table.
# Maintains insertion order.
# Average-case:
#   Lookup by key       O(1)
#   Insert              O(1)
#   Delete              O(1)
#   Move-to-end/popitem O(1)
# Space: O(n) for entries + linked-list pointers + hash table overhead.

# 6. deque (collections.deque)
# --------------------------------------------------
# Underlying: doubly-ended queue using blocks of memory.
# Average-case:
#   Append/appendleft    O(1)
#   Pop/popleft          O(1)
#   Indexing            O(n)
#   Insert/Delete in middle O(n)
# Space: O(n) for elements + small overhead for block pointers.

# 7. heapq (binary heap)
# --------------------------------------------------
# Underlying: list-based binary min-heap.
# Operations:
#   Push/pop            O(log n)
#   Peek                O(1)
#   Build-heap          O(n)
# Space: O(n)

# 8. bisect (sorted list operations)
# --------------------------------------------------
# Underlying: list + binary search.
# Operations:
#   Search insertion index O(log n)
#   Insert/Delete        O(n) (shifts elements)
# Space: O(n)

# 9. array.array (typed array)
# --------------------------------------------------
# Underlying: contiguous C-array of fixed types.\#   Access by index      O(1)
#   Search               O(n)
#   Append               O(1) amortized
# Space: O(n * element_size)

# 10. custom trees or linked lists (not builtin)
# --------------------------------------------------
#   Singly/Double linked list: insert/delete at head O(1), search O(n), space O(n)
#   Binary search tree: average lookup/insert/delete O(log n), worst-case O(n)
#   Balanced (AVL/Red-Black): lookup/insert/delete O(log n), space O(n)

# Summary of Big-O notation:
#   O(1)      constant time
#   O(log n)  logarithmic time
#   O(n)      linear time
#   O(n log n) linearithmic time
#   O(n^2)    quadratic time
# Space: typically O(n) unless otherwise noted.

# NOTE:
# - 'n' refers to the number of elements in the container.
# - Average-case for hash-based structures assumes a good hash distribution.
# - Worst-case for hash tables occurs under pathological collision sequences.
# - Amortized O(1) means occasional costly operations (resizing) spread over many cheap ones.


# 80/20 USAGE GUIDE
# --------------------------------------------------
# When approaching algorithmic problems, choose the data structure
# that optimizes your hot operations (~80% of your time), and avoid
# higher-complexity alternatives.
#
# 1. Two-sum or complement lookups
#    Use dict (hashmap): O(1) average lookup to check "seen" or complements.
#    Why: a naive nested loop is O(n^2), dict reduces this to O(n).
#
# 2. Sequential scans, in-place two-pointer techniques
#    Use list: O(1) indexing/appending for linear scans or swap-based in-place edits.
#    Why: converting to list and re-searching each element with index() would be O(n^2).
#
# 3. Membership tests or deduplication
#    Use set: O(1) average contains checks for sliding-window or counting uniques.
#    Why: list-based membership is O(n), making de-dup and lookups O(n^2) in worst cases.
#
# 4. Double-ended queue operations
#    Use deque: O(1) append/pop at both ends for sliding-window min/max or moving averages.
#    Why: using list popleft() is O(n), shifting all elements each pop.
#
# 5. Top-k selection
#    Use heapq: O(log k) per push/pop to maintain a fixed-size heap.
#    Why: sorting entire list is O(n log n), heap focuses operations on k, O(n log k).
#
# 6. Insertion-order retention + O(1) access
#    Use OrderedDict: O(1) lookup and O(1) move_to_end/popitem for LRU cache patterns.
#    Why: tracking order in a list plus dict is error-prone and list removals anywhere are O(n).
#
# 7. Sorted lookups with infrequent inserts
#    Use bisect + list: O(log n) for search, O(n) for insert.
#    Why: keeping items in a balanced tree gives O(log n) insert and search, but tree overhead
#          and Python packages cost more space; bisect is simpler when inserts are rare.
#
# 8. Fixed-type bulk numeric storage
#    Use array.array: O(1) access, memory-compact.
#    Why: list of numbers uses more memory and has same O(1) access, but array reduces space
#          and improves cache locality for large datasets.

# Thought Process:
# 1. Identify the hot operation: lookup? insert? pop? sort? linear scan?
# 2. Choose the structure with the best matching average-case O().
# 3. Compare against naive or alternative approach's complexity to justify choice.
# 4. Default to built-ins before custom implementations.
# End of 80/20 notes






# | Operation                         | dict          | set  | list                                | tuple           | array (from array module)           | linked list (LL)              |
# | --------------------------------- | ------------- | ---- | ----------------------------------- | --------------- | ----------------------------------- | ----------------------------- |
# | **Lookup (by key/index/element)** | O(1) (by key) | O(1) | O(1) (by index), O(n) (by value)    | O(1) (by index) | O(1) (by index)                     | O(n) (by value/index)         |
# | **Insertion**                     | O(1)          | O(1) | O(1) (append), O(n) (insert middle) | N/A (immutable) | O(1) (append), O(n) (insert middle) | O(1) (at head), O(n) (middle) |
# | **Deletion**                      | O(1)          | O(1) | O(n) (by value/index)               | N/A (immutable) | O(n) (remove)                       | O(1) (at head), O(n) (middle) |
# | **Space Complexity**              | O(n)          | O(n) | O(n)                                | O(n)            | O(n)                                | O(n)                          |
# | **Iteration**                     | O(n)          | O(n) | O(n)                                | O(n)            | O(n)                                | O(n)                          |

# ---dict/set--: Hash tables, fast lookup/insertion/deletion by key or element.
# ---list------: Dynamic arrays, fast index access, slow insert/delete except at end.
# ---tuple-----: Immutable lists, fast index access, no insert/delete.
# ---array-----: Like list but fixed type, more memory efficient.
# ---linked L--: Nodes with pointers, slow random access, fast insert/delete if node known.