# x ='hello world'
# list(x) # unpacking string into a list
# new_x = ''.join(x) # repacking list x and concatenating into single string
# print(new_x)




dial_codes = [
    (880, 'Bangladesh'),
    (55, 'Brazil'),
    (86, 'China'),
    (91, 'India'),
    (62, 'Indonesia'),
    (81, 'Japan'),
    (234, 'Nigeria'),
    (92, 'Pakistan'),
    (7, 'Russia'),
    (1, 'United States'),
]

country_codes = {country: code
                 for code, country in dial_codes}

# print({code: country.upper()
#        for country, code in sorted(country_codes.items())
#        if code <= 91})






types = ['toyota', 'bmw', 'honda', 'ford', 'chevy']
nums = [10,11,12,13,14]
trucks = { name: model for name, model in zip(types, nums) } # you must pair two lists in this situation
### or 
cars = dict(zip(types, sorted(nums, reverse=True))) # just use the dict constructor
# cars = {i for i in types} # dict comp for a set
# print(cars)
# print(trucks)
# print(trucks.popitem())

# NOTE: unpacking mappings
#Remember duplicate keyword args are forbidden
# ** means to unpack dict into keyword arguments
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
e = {'z': 88, 'f': 45, 'w': 33, 'i': 44, 'p': 557}

def dump(**kwargs):
    return kwargs

# print('kwargs', dump(**d, **e, r=98))
# or
# print('merge mapping with |', d | e)

# to change mapping in place 
d |= e # d =  d + e
# print('merge mapping in place with |=', d)





# NOTE: Match case

# takes a dict, returns a list
# a useful practice for handling semi-structured data like JSON records
def get_creators(record: dict) -> list:
    match record:
        case {'type': 'book', 'api': 2, 'authors': [*names]}:
            return names
        case {'type': 'book', 'api': 1, 'author': name}:
            return [name]
        case {'type': 'book'}:
            raise ValueError(f"Invalid 'book' record: {record!r}")
        case {'type': 'movie', 'director': name}:
            return [name]
        case _:
            raise ValueError(f'Inval record: {record!r}')

an_examp = dict(api=1, author='Douglas Hofstadter',
         type='book', title='Gödel, Escher, Bach')
print(get_creators(an_examp)) # notice order is irrelevant


# to capture extra key-value pairs: **details
food = dict(category='ice cream', flavor='vanilla', cost=199)
match food:
    case {'category': 'ice cream',
    **details}: 
        print(f'Ice cream details: {details}')



# a set is mutable, a frozen set is imutable. 
# cannot be modified after creation()
toyota = frozenset([1,2,3,4,3])
print('frozenset', toyota)










"""
DEFINITIONS
"""
def example_func(pos1, pos2, *, kw1=None, kw2=None, **kwargs):
    """
    Parameters:
    - pos1, pos2: positional or keyword parameters (can be passed as arguments by position or name)
    - kw1, kw2: keyword-only parameters (must be passed using name=value)
    - **kwargs: captures any extra keyword arguments in a dict
    """
    print("pos1:", pos1)      # argument passed to parameter 'pos1'
    print("pos2:", pos2)      # argument passed to parameter 'pos2'
    print("kw1:", kw1)        # argument passed to keyword-only parameter 'kw1'
    print("kw2:", kw2)        # argument passed to keyword-only parameter 'kw2'
    print("kwargs:", kwargs)  # extra keyword arguments as a dict

"""
QUESTIONS
"""
# what is 32 to 64 bits(my computer?compiler? hardware?)