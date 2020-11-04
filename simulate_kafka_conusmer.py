import threading, queue
import time


def asyc_queue(q, data):
    def worker():
        while True:
            if not globals()[q].empty():
                data = globals()[q].get()
                time.sleep(4)
                print(data)
            # q1.task_done()

    try:
        globals()[q].put(data)
    except:
        print("new queeue is created")
        globals()[q]= queue.Queue()
        threading.Thread(target= worker).start()
        globals()[q].put(data)


i = 0 
while True:
    i= i +1
    asyc_queue("q1", i)
    # asyc_queue("q2", i+10)

    print("--------------kafka consumer-------------\n")
    time.sleep(1)

print("done")