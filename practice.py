
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





# s = "alien man"

# def capitalize_words(x):
#     words = x.split()
#     print(words)

#     capw = [word.capitalize() for word in words]
#     print(capw)

#     result = ' '.join(capw)

#     return result

# print(capitalize_words(s))




# s = "programming"
# map = {}
# total_sum = 0

# for x in s:
#     if s not in map:
#         map[x] +=1

# print(map)


# s = "programming"
# map = {}

# for x in s:
#     if x not in map:
#         map[x] = 1
#     else:
#         map[x] += 1

# print(map)

# s = [1,2,2,2,3,4,5,6]
# dic = {}

# for x in s:
#     if x not in dic:
#         dic[x] = 1
#     else:
#         dic[x] +=1
# print(dic)

# fruit = ["apple", "banana", "kiwi", "cherry", "melon"]
    
# def a(s: list):
#     map = {}
#     index = 0

#     for i in s:
#         map[index] = len(i)  
#         index += 1
#     return map
# #another way to write this
# # from collections import Counter
# # def count_string_lengths(strings):
# #     lengths = [len(s) for s in strings]
# #     return dict(Counter(lengths))
# print(a(fruit))

# array = [1,3,5,2,8]

# def func(x: list):
#     highest_value = x[0]
#     ptr = 0
    

#     for i in x:
#         if i > ptr:
#             ptr = i
#             if ptr > highest_value and ptr != i:
#                 highest_value = ptr
#                 ptr = highest_value

#     return ptr * highest_value

# print(func(array))



arr = [1,3,5,2,8]
# def max_product(x: list)-> int:
#     arr.sort()
#     return arr[-1] * arr[-2]


# print(max_product(arr))

def func(x: list)-> int:
    # max1 = float('-inf')
    # max2 = float('-inf')
    max1 = 0
    max2 = 0

    for num in x:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
    
    return max1 * max2

print(func(arr))




# got it. once I finish this question, let's focus on looping questions using while 
# loops. or, questions involving more boolean values. 
