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

# print(dial_codes)

country_codes = {country: code
                 for code, country in dial_codes}

print({code: country.upper()
       for country, code in sorted(country_codes.items())
       if code <= 91})




types = ['toyota', 'bmw', 'honda', 'ford', 'chevy']
nums = [10,11,12,13,14]
trucks = { name: model for name, model in zip(types, nums) } # you must pair two lists in this situation
### or 
cars = dict(zip(types, sorted(nums, reverse=True)))


# cars = {i for i in types} # dict comp for a set


print(cars)
