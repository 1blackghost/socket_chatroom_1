import socket
from _thread import *

clients = []
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 6535))
s.listen(5)


def recv(a, c):
    while True:
        try:

            msg = a.recv(1024)
            print("msg recv", msg.decode("utf-8"))
            try:
                for i in clients:
                    i.send(msg)
            except:
                pass
        except Exception as e:
            print(str('[-]')+str(e))


while True:
    a, c = s.accept()
    clients.append(a)
    print("[+]connection accepted")
    start_new_thread(recv, (a, c))
