lax_coordinates = (33.9425, -118.408056)
lat, long = lax_coordinates # unpacking
print(lat)


x = [1,2,3,4]
first, second, third, fourth = x
print(second, fourth)

# also use * to unpack... it unpacks the d.struct into
# individual elements, instead of directly passing them
print(divmod(20, 8))
# divmod does quotient then remainder
# 20 // 8 = 2
# 20 % 8 = 4
t = (20, 8)
print(divmod(*t))

from ast import parse
import os 
_, filename = os.path.split('/Users/marmossburg/Desktop/python_edu/fluent_python')
print(filename) # prints fluent_python


# Grab Excess items with *
a, b, *rest = range(5)
print(rest)


# nested unpacking
metro_areas = [
('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

def nested_unpacking():
    print('----------------------------------')
    for name, _, _,(lat, lon) in metro_areas:
        if lon <= 0: # tests only cities in western hemishpere
            print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')
    print('----------------------------------')

nested_unpacking()



print('----------------------------------')
nums = [1,2,3,4,5]
print(*nums)



