import threading
import time
import random
import queue



class ConsumerThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(ConsumerThread,self).__init__()
        self.target = target
        self.name = name
        return

    def run(self):
        while True:
            if not globals()[q].empty():
                item = globals()[q].get()

                text_file = open(q +  "/" + str(item) + ".txt", "w")
                text_file.close()
        return

if __name__ == '__main__':
    q= 'data1'
    globals()[q]= queue.Queue()
    globals()[q].put(1)
    globals()[q].put(2)

    ConsumerThread().start()


    print("done")