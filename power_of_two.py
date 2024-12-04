def p_o_two(n: int)-> bool:
    return n > 0 and (n & (n-1) == 0)

# n & (n-1) is a bitwise operation 
# powers of two have one bit set to 1 --> 0001, 2 --> 0010
#This is a bitwise operation 
