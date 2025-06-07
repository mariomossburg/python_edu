# how it works
# it recurses down to the base case. adding to the call stack
# Using LIFO, the call stack works at base case popping(.pop()) until reaching n
# then it multiplies until the final answer:
# factorial(4) --> returns 4 * 6 = 24

def factorial(n):
    if n == 0:  
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case

print(factorial(4))  



