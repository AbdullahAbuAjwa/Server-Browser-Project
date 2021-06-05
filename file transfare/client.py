import socket
import sys

HOST = socket.gethostname()
PORT = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print("Connected with Server")

f_send = "file.txt"
with open(f_send, "rb") as f:
    print("Send file:")
    data = f.read()
    s.sendall(data)
    s.close()
    print("Disconnected")
    sys.exit(0)
