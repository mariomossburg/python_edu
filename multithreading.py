import threading, time



def thread_one():
    for i in range(8):
        print('as thread one, i do requests')
        time.sleep(1)

def thread_two():
    for i in range(2):
        time.sleep(4)
        print('as thread two, i update things')


def thread_three():
    for i in range(1):
        time.sleep(8)
        print('as thread 3, i run health checks')

a = threading.Thread(target=thread_one)
b = threading.Thread(target=thread_two)
c = threading.Thread(target=thread_three)

a.start()
b.start()
c.start()