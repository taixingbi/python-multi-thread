import threading, queue
import time

q = queue.Queue()


def worker():
    while True:
        item = q.get()
        print( item, "Working on")

        text_file = open( str(item) + ".txt", "w")
        text_file.close()

        print( item, "Finished" )

        q.task_done()


threading.Thread(target=worker).start()

data1=['a','b','c','d','e']
data2=['aa','bb','cc','dd','ee']

for item in range(5):
    q.put(item)
    
print('job start\n')

q.join()

print('\njob done')