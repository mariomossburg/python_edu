hashmap = {'name': 'python', 'computer': 'apple', 'gpu': 'nvidia', 'cpu': 'amd'}

print("-----------print keys-----------------")
for x in hashmap:
    print(x)


print("-----------print values-----------------")
for x in hashmap:
    print(hashmap[x])

print("-----------print values-----------------")
print("-----------.values()-----------------")

for x in hashmap.values():
    print(x)


print("-----------print values-----------------")
print("-----------.keys()-----------------")
for x in hashmap.keys():
    print(x)


print("-----------print keys and values-----------------")
for x, y in hashmap.items():
    print(x," " ,y)









