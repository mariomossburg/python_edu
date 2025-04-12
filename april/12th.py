

# miso = [9,8,7,6,5,4,3,2,1]
# viso = []

# print(miso)

# for i in len(miso):
#     viso.append(miso.pop())


# while miso:
#     viso.append(miso.pop())

# print(viso)



def is_valid(s:str)->bool:
    stack = []
    close_to_open = {")": "(", "]": "[", "}": "{" }

    for c in s:
        if c in close_to_open:
            if stack and stack[-1] == close_to_open[c]:
                stack.pop()
            else:
                return False 
        else:
            stack.append(c)
    return True if not stack else False



    


