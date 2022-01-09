import socket
from _thread import *

clients = []
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("0.tcp.ngrok.io", 16004))
except:
    print("[-]ERROR")
    input()
print("[+]STATUS:CONNECTED")
print("WELCOME TO MASTERCHAT!!V1.0")

def recv():
    while True:
        try:
            msg = s.recv(1024)
            print(msg.decode('utf-8'))
        except:
            pass


start_new_thread(recv, ())
name = input("Enter your name: ")
s.send(str(name)+" Joined".encode("utf-8"))
print("<Type In the Message and press enter to send...>\n")
while True:
    msg = input("")
    try:
        s.send(str(str(name)+str(":")+ str(msg)).encode('utf-8'))
    except:
        pass
