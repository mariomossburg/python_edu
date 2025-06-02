a  = set(i for i in range(6))
b = set(i for i in range(3,9)) 
c = set(i for i in range(3))
print('a', a)
print('b', b)
print('difference:', a.difference(b)) # in a not in b
print('union:', a.union(b)) # all of a and b together
print('intersection:', a.intersection(b)) # elements that exist in between both sets
print('isdisjoint: ', a.isdisjoint(b)) # if both sets have no intersection
print('symmetric difference', a.symmetric_difference(b)) # elements of both a, b that don't intersect
print('issubset:', c.issubset(a)) # all elements in c exist within a
print('is superset: ', a.issuperset(c)) # inverse of subset
# print(len(a) - len(c))



