# List comprehension and generator expressions


# List comprehension: a concise to create a list 
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


