import threading
import time

def thread_job(job):
    time.sleep(2)
    print(job)

if __name__ == "__main__":
    x = threading.Thread(target=thread_job, args=("this is job",))
    x.start()
    print("done")
