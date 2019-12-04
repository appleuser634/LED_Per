import threading
import time

def loop_0():
    
    for i in range(10):
        print("loop_0:",i)
        time.sleep(0.5)
def loop_1():
    
    for i in range(10):
        print("loop_1:",i)
        time.sleep(0.5)
def loop_2():
    
    for i in range(10):
        print("loop_2:",i)
        time.sleep(0.5)

def loop_3():
    
    for i in range(10):
        print("loop_3:",i)
        time.sleep(0.5)

def loop_4():
    
    for i in range(10):
        print("loop_4:",i)
        time.sleep(0.5)

def loop_5():
    
    for i in range(10):
        print("loop_5:",i)
        time.sleep(0.5)

thread_0 = threading.Thread(target=loop_0)
thread_1 = threading.Thread(target=loop_1)
thread_2 = threading.Thread(target=loop_2)
thread_3 = threading.Thread(target=loop_3)
thread_4 = threading.Thread(target=loop_4)
thread_5 = threading.Thread(target=loop_5)

thread_0.start()
time.sleep(1)
thread_1.start()
time.sleep(1)
thread_2.start()
time.sleep(1)
thread_3.start()
time.sleep(1)
thread_4.start()
time.sleep(1)
thread_5.start()
time.sleep(1)
