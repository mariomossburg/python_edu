# List Comprehension  builds the whole list in memory at once.
squares = [x * x for x in range(3)]
print(squares)  # [0, 1, 4]

# has all built in functions available, len(), etc...


#generator expression
# It doesn’t build the list—it gives you one item at
# a time when you ask for it (lazy). 
# uses next(), and and is wrapped in ()
# no memory used for whole list


gen = (x * x for x in range(3))
print(next(gen))
print(next(gen))



# [x * x for x in range(1000)]: holds 1000 results in memory.
# (x * x for x in range(1000)): computes only one at a time.

# unpacking and destructuring? ellipsis (...) notation?

# pattern matching in python is great






# reading: Eli Bendersky’s blog post “Less copies in Python with the buffer protocol and memo‐
# ryviews” includes a short tutorial on memoryview.
#reference pg.72 for more