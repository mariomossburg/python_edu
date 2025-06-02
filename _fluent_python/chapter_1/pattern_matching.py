
metro_areas = [
('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

#method of pattern matching... returns None
def matching():
    for record in metro_areas:
        match record:
            case [name, _, _, (lat, lon)] if lon <=0:
                print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')


print(matching())


# using the method of unpacking
# def nested_unpacking():
#     print('----------------------------------')
#     for name, _, _,(lat, lon) in metro_areas:
#         if lon <= 0: # tests only cities in western hemishpere
#             print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')
#     print('----------------------------------')

# nested_unpacking()





# method from an imaginary robot class
# def handle_command(self, message):
#         match message:
#                 case ['BEEPER', frequency, times]:
#                     self.beep(times, frequency)
#                 case ['NECK', angle]:
#                     self.rotate_neck(angle)
#                 case ['LED', ident, intensity]:
#                     self.leds[ident].set_brightness(ident, intensity)
#                 case ['LED', ident, red, green, blue]:
#                     self.leds[ident].set_color(ident, red, green, blue)
#                 case _:
#                     raise InvalidCommand(message)