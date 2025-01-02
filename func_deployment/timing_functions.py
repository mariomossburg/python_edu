import time

# you can also use cprofile for a more indepth timing 
# import cprofile
# cProfile.run('()')


right_now = time.ctime()
# round(right_now, 2) # second argument is decimal points
print(right_now)



def function_timing():
    product = 1
    start_time = time.time()
    for i in range(1000000):
        product = product * i
    end_time = time.time()
    print(f'the function took {end_time - start_time} to run')

function_timing()



# import time

# # Display the program's instructions.
# print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
# input()                    # press Enter to begin
# print('Started.')
# startTime = time.time()    # get the first lap's start time
# lastTime = startTime
# lapNum = 1
