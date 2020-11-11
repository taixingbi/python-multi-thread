import threading
import time

g_value = 0
def f1():
    global g_value
    print ("f1 ", g_value)
    g_value= 1

def f2():
    global g_value
    time.sleep(1)
    print ("f2 ", g_value)

threading.Thread(target=f1).start()
threading.Thread(target=f2).start()