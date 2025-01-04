# tuples are immutable in nature, however,the immutability only applies to 
# the references contained in it. more simply, a tuple can reference a mutable list
# where it's values are mutable
a = (10, 'alpha', [1,2])
b = (10, 'alpha', [1,2])
print(a==b)
b[-1].append(99)
print(a==b)
print(b)

print('-------------------')
# determine explicitly if a tuple has a fixed value
# an object is hashable if hash value doesn't change during it's lifetime
def fixed(o):
    try:
        hash(o)
    except TypeError:
        return False
    return True


tf = (10, 'alpha', (1,2)) # (1,2) is a nested tuple, therefore not mutable,
tm = (10, 'alpha', [1,2]) # unhashable, contains mutable object--> list
print(fixed(tf))
print(fixed(tm))

# bottom lines are the same
print(tf.__contains__('alpha'))
print('alpha' in tf)
