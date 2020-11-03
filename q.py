import threading, queue
import time

q = queue.Queue()

def worker():
    while True:
        item = q.get()
        print( item, "Working on")
        time.sleep(4)

        print( item, "Finished" )
        print( "\n" )

        q.task_done()

threading.Thread(target=worker).start()


for item in range(5):
    q.put(item)
    
print('job start')

q.join()

print('job done')