# cast the integer to a string, where it can then be 
# manipulated since a string is a data structure
s = str(456)
print(s[::-1])



a = 456
# str(a) this line will not work 
# since it has no assignment it is merely 
# a function that doesn't sign a result to a
a = str(a)
print(a[::-1])