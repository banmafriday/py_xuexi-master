# coding:utf-8
from threading import Thread
from socket import *

# 接收信息
def recvData():
    msg = s.recv(1024)
    print(">>",msg.decode())

# 发送信息
def sendData():
    info = input("<<:")
    s.sendto(info.encode(),(ip,port))

ip = "localhost" # 对方ip
port = 9002 # 对方端口号

s = socket(AF_INET,SOCK_RAW)
s.bind(("localhost",9001))

tr = Thread(target=recvData())
t2 = Thread(target=sendData())
tr.start()
t2.start()