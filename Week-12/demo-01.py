# Connect to a web site and accept the content

import socket
import time
start = time.time()
spt = time.process_time()
spc= time.perf_counter()

server = 'www.hackthissite.org'
port = 443

ip = socket.gethostbyname(server)
print("HOST: {} IP: {} PORT: {}".format(server, ip, port))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))

request = "GET / HTTP/1.1\nHost: " + server + "\n"

s.send(request.encode())
result = s.recv(1024)

print(result)

end = time.time()
ept = time.process_time()
epc = time.perf_counter()
print("Seconds     : {}".format(end - start))
print("Proc Counter: {}".format(ept - spt))
print("Perf Counter: {}".format(epc - spc))
