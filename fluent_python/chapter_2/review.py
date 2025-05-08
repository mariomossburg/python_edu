import array 

arr = array.array('i', [0] * 10)


for i in range(len(arr)):
    arr[i] = i
print(arr)



board = [['_'] * 3 for i in range(3)  ]
print(board)

board[0][1] = 'x'
board[1][1] = 'x'
board[2][1] = 'x'
for row in board:
    print(row)
    
    
a_new_list = [i for i in range(20)]
print(a_new_list)

import time

start_time = time.time()
gen_expression = (i for i in range(20))  # Generator expression

# Get the next item initially
next_item = next(gen_expression)

while next_item is not None:
    current_time = time.time()

    # Check if 1 second has passed since last print
    if current_time - start_time >= 1:
        print(f'Next? {next_item * 2}')
        start_time = current_time  # Reset start time to control timing
        
        # Try to get the next value from the generator
        try:
            next_item = next(gen_expression)
        except StopIteration:
            next_item = None  # End loop if generator is exhausted
