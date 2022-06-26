import socket
import os

ip = "192.168.56.102"
port = 8778
buf_size = 4096
SEP = "<SEPERATE>"
s = socket.socket()
s.bind(('',port))
s.listen(5)
print(f"Listening as {ip}:{port}")
c_s, address = s.accept()
print(f"{address} is being connected")
try:
    fname = c_s.recv(buf_size).decode()
    fsize = c_s.recv(buf_size).decode()
    fname = os.path.basename(fname)
    fsize = int(fsize)
    with open(fname, "wb") as f:
        while True:
            bytes_read = c_s.recv(buf_size)
            if not bytes_read:
                break
            f.write(bytes_read)
except:
    print("Error Been Occured. Terminating Server...")
c_s.close()
s.close()
