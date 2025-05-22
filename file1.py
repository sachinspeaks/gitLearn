import threading
import time
print("Starting in file1")

def printTem():
    print("Begin")
    time.sleep(1)
    print("Finish")

thread2=threading.Thread(target=printTem)

thread2.start()