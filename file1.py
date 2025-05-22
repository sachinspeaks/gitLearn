import threading
import time
print("Starting in file1")

def printTem():
    print("Started")
    time.sleep(1)
    print("Done")

thread1=threading.Thread(target=printTem)

thread1.start()