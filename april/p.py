









def count_vowels(s:str)->int:
    vowels = ['a','e','i','o','u']
    count = 0

    for i in s:
        if i in vowels:
            count +=1

    return count

print(count_vowels('greater than ever'))


# def second_largest(nums:list)->int:
#     sl_num = []

#     for i in nums:
#         if sl_num < i:
#             sl_num = i
#     return sl_num

nums = [3,2,7,4,11,8]

# print(second_largest(nums))



def remove_odd(nums:list) -> list:
    new_list = []

    for i in nums:
        if i % 2 == 0:
            new_list.append(i)
    return new_list


print(remove_odd(nums))





# def iss_prine(n:int)->bool:
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False 
#     return True




# print(iss_prine(10))

# Return types:
# def get_number() -> int:
#     return 42

# def get_price() -> float:
#     return 19.99

# def is_active() -> bool:
#     return True

# def get_name() -> str:
#     return "Alice"

# def get_list() -> list:
#     return [1, 2, 3]

# def get_tuple() -> tuple:
#     return (1, 2, 3)

# def get_dict() -> dict:
#     return {"key": "value"}

# def get_set() -> set:
#     return {1, 2, 3}

# def do_nothing() -> None:
#     return
