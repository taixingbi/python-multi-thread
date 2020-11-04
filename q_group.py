import threading, queue
import time

def worker():
    while True:
        if not globals()[q].empty():
            data = globals()[q].get()
            time.sleep(4)
            print(data)

        # globals()[q].task_done()

q= 'queenJob'
globals()[q]= queue.Queue()
globals()[q].put(0)
globals()[q].put(1)

threading.Thread(target= worker ).start()

print("done")