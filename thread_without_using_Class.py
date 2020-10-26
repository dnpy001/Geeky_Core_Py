# #    thread_without_using_Class.py
# from threading import Thread
# 
# 
# def disp(a, b):
#     print("Thread Running", a, b)
# 
#     
# t = Thread(target=disp, args=(10, 20))
# t.start() 

# with for loop

#    thread_without_using_Class.py
from threading import Thread


def disp(a, b):
    print("Thread Running", a, b)


for i in range(5):    
    t = Thread(target=disp, args=(10, 20))
    t.start() 
    print()
print("Happy Coding")
