import sys

def square(x):
    return x ** 2

def cubed(x):
    return x ** 3

num = float(sys.argv[1])
print("Cmdln arg squared", square(num))
print("Cmdln arg cubed", cubed(num))

