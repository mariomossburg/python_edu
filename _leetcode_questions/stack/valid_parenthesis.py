s = ''

# Valid parenthesis... all need to be correctly opened and closed

"""

"""

def func(s:str)-> bool:
    stack = []
    closeToOpen = {")": "(", "]": "[", "}": "{" }
    
    for c in s:
        if c in closeToOpen:
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                return False
        else: 
            stack.append(c)
    return True if not stack else False


m = "{[1]}"
# print(func(m))




# ana = "ana"
# x = 5
# y = 3.77

# s = input()

# def talk(s: str):
#     # s = input()
#     greet = "Hello, my name is " + s
#     return greet
    
# print(talk(s))







# nombre = ["ana", "cardozo"]
# print(nombre[-1])

# def 



