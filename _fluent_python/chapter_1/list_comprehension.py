# List comprehension and generator expressions


# List comprehension: a concise way to create a list 
# by applying an expression to elements from an iterable
# brackets
s = [x**2 for x in range(5)]
print(s)

# Generator Expression: creates a generator, but lazily(on-demand)
# use for large datasets to save memory, large datasets
# parenthesis
squares = (x**2 for x in range(5))
print(next(squares)) # output = 0


# walrus operator:
# do two things at the same time. remain accessible outside of scope

# basic example with and without
x = 10
if x > 5:
    print("it is greater")

if(x := 10) > 5:
    print('we used walrus here')






# example from book
# without
x = 'ABC'
codes = [ord(x) for x in x]
print(x)
print(codes)

codes = [last := ord(c) for c in x]
print(last)


print('--------------------------------')
print('\n\n')

nums = [1,2,3,4,5,6]
new_list = [num for num in nums]
print(new_list)

colors = ['black', 'white']
sizes = ['s', 'm', 'l']
# tshirts = [(color, size) for color in colors for size in sizes]
# print(tshirts)


print('--------------------------------')
print('\n\n')
# prints each item line by line
for tsh in (f'{c} {s}' for c in colors for s in sizes):
    print(tsh)