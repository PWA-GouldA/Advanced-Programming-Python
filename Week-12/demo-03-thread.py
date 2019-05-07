import threading
from queue import Queue

thread_lock = threading.Lock()


def threader():
    while True:
        worker = q.get()    # Fetch the port from the eorker for loop

        p_scan(worker)      # Calls the portscan method
                            # and pass the port number

        q.task_done()       # Called when task is completed


q = Queue()                 # It will create the queue and the threader

for p in range(50):         # It defines the number of threads to run
    t = threading.Thread(target=threader)

    t.daemon = True         # This is consider thread as daemon,
                            # so if the main thread dies it will also die

    t.start()               # start the tread

for worker in range(1, 100):
    q.put(worker)           # this is the port number to be scanned
                            # from 1 to 100

q.join()                    # It waits until the thread terminates
