# Bit Manipulation

# Benefits: 
# Efficient: faster than arithmetic operations for certain tasks (checking even/odd, power of two).
# Memory Optimization: Bits take less space than larger data types.
# Control: allows fine-grained control over data.



#------------OPERATORS--------------
#
# -- AND (&) -> Zeroes out bits that don't match.
# -- OR (|) → Turns on a bit if at least one operand has it set.
# -- XOR (^) → Toggles bits where operands differ.
# -- NOT (~) → Inverts all bits.
# -- Left Shift (<<) → Shifts bits to the left (multiplies by 2).
# -- Right Shift (>>) → Shifts bits to the right (divides by 2).


#------------NUMBERS AND THEIR VALUES--------------
#
# Decimal  |  Binary   | Bit Value Representation               | Explanation
# -------- | --------- | -------------------------------------- | ----------------------------------------------
# 1        | 0001      | 2^0 = 1                                | 1 is represented as 2^0
# 2        | 0010      | 2^1 = 2                                | 2 is represented as 2^1
# 3        | 0011      | 2^1 + 2^0 = 3                          | 3 is 2^1 + 2^0
# 4        | 0100      | 2^2 = 4                                | 4 is represented as 2^2
# 5        | 0101      | 2^2 + 2^0 = 5                          | 5 is 2^2 + 2^0
# 6        | 0110      | 2^2 + 2^1 = 6                          | 6 is 2^2 + 2^1
# 7        | 0111      | 2^2 + 2^1 + 2^0 = 7                    | 7 is 2^2 + 2^1 + 2^0
# 8        | 1000      | 2^3 = 8                                | 8 is represented as 2^3
# 9        | 1001      | 2^3 + 2^0 = 9                          | 9 is 2^3 + 2^0
# 10       | 1010      | 2^3 + 2^1 = 10                         | 10 is 2^3 + 2^1
# 11       | 1011      | 2^3 + 2^1 + 2^0 = 11                   | 11 is 2^3 + 2^1 + 2^0
# 12       | 1100      | 2^3 + 2^2 = 12                         | 12 is 2^3 + 2^2
# 13       | 1101      | 2^3 + 2^2 + 2^0 = 13                   | 13 is 2^3 + 2^2 + 2^0
# 14       | 1110      | 2^3 + 2^2 + 2^1 = 14                   | 14 is 2^3 + 2^2 + 2^1
# 15       | 1111      | 2^3 + 2^2 + 2^1 + 2^0 = 15             | 15 is 2^3 + 2^2 + 2^1 + 2^0


def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0



def find_unique(nums):
    result = 0
    for num in nums:
        result ^= num
    return result


x = 10
print(x.__sizeof__())