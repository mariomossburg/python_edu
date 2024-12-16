# Type conversion changes one data type to another
arr = [1,2,2,3]
set(arr)
# dict(arr) # TypeError: cannot convert dictionary update sequence element #0 to a sequence

x = '1223'
int(x) # strong to int


# implicit conversion
x = 5
y = 2.5
result = x+y # implicitly converts to float


# why are they important?
# ----   accurate comparisons
# ----   data integration --> important when data is in diff formate like. i.e. crawling, converting str to int
# ----   error avoidance and bugs
# ----   flexibility. i.e. sum(list(nums)) when nums is a set
#   




