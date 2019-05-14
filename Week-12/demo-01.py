# Connect to a web site and accept the content

import socket
import time
start = time.time()
spt = time.process_time()
spc= time.perf_counter()

hostname = 'a106-20'
port = 80

ip = socket.gethostbyname(hostname)
print("HOST: {} IP: {} PORT: {}".format(hostname, ip, port))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))

request = "GET / HTTP/1.1\nHost: " + hostname + "\n"

s.send(request.encode())
result = s.recv(1024)

print(result)

end = time.time()
ept = time.process_time()
epc = time.perf_counter()
print("Seconds     : {}".format(end - start))
print("Proc Counter: {}".format(ept - spt))
print("Perf Counter: {}".format(epc - spc))
