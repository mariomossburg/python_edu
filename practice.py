
# s = [1,2,3,4,5,6]
# sum = 0

# for i in s:
#     # if i % 2 == 0: # for summing even
#     if i % 2 != 0: # odd
#         sum += i

# print(sum)
    
# another way to write this
# This uses generator expression
# sum_of_even = sum(i for i in s if i % 2 == 0)
# print(sum_of_even)

# s = "hello world"
# s = "aeiou"
# sum = 0
# vowels = { "a", "e", "i", "o", "u"}

# for i in s:
#     if i not in vowels:
#         sum += 1

# print(sum)


# s = "Hello World"
# sum = 0

# for i in s:
#     if i.isupper():
#         sum += 1

# list  = []
# for i in s:
#     if i.isupper():
#         list.append(i)

# print(sum)
# print(list)


# def f(x):
#     if x == 0:
#         return 1
#     else:
#         return x * f(x-1)

# print(f(5))

# numbers = [3,1,4,1,5,9,2,6]

# def max_in_list(numbers: list):
#     max = numbers[0]
#     for i in numbers:
#         if i > max:
#             max = i
#     return max

# print(max_in_list(numbers))

# fruits = ["apple", "banana", "cherry", "kiwi", "strawberry"]

# def mx_ln(a: list):
#     for i in a:
#         max_length = a[0]
#         if len(i) > len(max_length):
#             max_length = i

#     return max_length

# print(mx_ln(fruits))


s = "alien man"

def capitalize_words(x):
    words = x.split()
    print(words)

    capw = [word.capitalize() for word in words]
    print(capw)

    result = ' '.join(capw)

    return result

print(capitalize_words(s))




# def capital(x):
#     new_capital = x


# print(capital(s))

