import threading, queue
import time

def worker():
    while True:
        if not q.empty():
            data = q.get()
            time.sleep(1)
            print(data)

q= queue.Queue()
q.put(0)
q.put(1)

threading.Thread(target= worker ).start()

print("done")