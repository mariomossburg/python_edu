# binary search is most successful with log n time

# brute force
# def mySqrt(x: int) -> int:
#     i = 0
#     while (i*i) <= x:
#         i+=1
#     return i -1

def mySqrt(x: int) -> int:
    l,r = 0, x
    res = 0

    while l <= r:
        m = l + ((r - 1) // 2)

        if m **2 > x:
            r = m-1
        elif m **2 < x:
            l = m + 1
            res = m
        else:
            return m


