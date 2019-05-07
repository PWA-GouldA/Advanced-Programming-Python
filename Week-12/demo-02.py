# Connect to a web site and accept the content

import socket
import time

# function to probe a port
def port_scan(port):
    try:
        con = s.connect((ip, port))
        return True
    except:
        return False


server = 'localhost'
port_start = 1
port_end = 80
port_count = port_end - port_start + 1

time_start = time.time()

ip = socket.gethostbyname(server)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("HOST: {} IP: {}".format(server, ip))
print("Scanning {} ports ({} to {})".format(port_count, port_start, port_end))

for port_num in range(port_start, port_end+1):
    if port_scan(port_num):
        print('\nPort {} is open'.format(port_num))

time_end = time.time()
time_diff = time_end - time_start
ports_per_second = time_diff / port_count
print("\nCompleted in {} seconds ({} ports per second)".format(time_diff, ports_per_second))
