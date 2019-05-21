# Connect to a web site and accept the content

import socket
import time
import threading
from queue import Queue


# function to probe a port
def port_scan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((ip, port))
        with thread_lock:
            print('Port {} is open'.format(port))
        con.close()
    except:
        pass


def threader():
    while True:
        worker = q.get()  # Fetch the port from the worker for loop
        port_scan(worker)  # Calls the port_scan method and pass the port number
        q.task_done()  # Called when task is completed


server = 'a133-11'
port_start = 1
port_end = 65535
port_count = port_end - port_start + 1

time_start = time.time()

thread_lock = threading.Lock()

ip = socket.gethostbyname(server)

print("HOST: {} IP: {}".format(server, ip))
print("Scanning {} ports ({} to {})".format(port_count, port_start, port_end))

q = Queue()  # It will create the queue and the threader

for p in range(4096):  # It defines the number of threads to run
    t = threading.Thread(target=threader)
    t.daemon = True  # This is consider thread as daemon, so if the main thread dies it will also die
    t.start()  # start the tread

for worker in range(port_start, port_end + 1):
    q.put(worker)  # this is the port number to be scanned (port_start to port_end)

q.join()  # It waits until the thread terminates

time_end = time.time()
time_diff = time_end - time_start
ports_per_second = time_diff / port_count
print("\nCompleted in {} seconds ({} ports per second)".format(time_diff, ports_per_second))
