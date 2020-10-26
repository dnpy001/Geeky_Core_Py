# with loop, thread2
from threading import Thread


def disp(a, b):
    for i in range(5):
        print("Child Thread")

    
t = Thread(target=disp, args=(10, 20))
t.start() 

for i in range(5):
    print("Main Thread")
    print("Happy Coding")

print("No Control of order for threads...")
