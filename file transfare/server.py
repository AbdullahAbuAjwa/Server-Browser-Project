import socket
import sys


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 8080))
s.listen(5)


print("Listening: ")

while True:
    conn, addr = s.accept()
    print("Client connected: ", addr)

    f = open("newFile.txt", "wb")
    while True:
        data = conn.recv(4096)
        if not data:
            break
        f.write(data)
    f.close()
    print("[+]")