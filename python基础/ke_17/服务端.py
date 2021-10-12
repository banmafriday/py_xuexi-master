# coding:utf-8
# 服务端,接口消息
from socket import *
s =socket(AF_INET,SOCK_DGRAM)

# 绑定监听端口
s.bind(("localhost",6363))

#监听客户端发来的消息
s.listen()

#等待消息
conn,adr=s.accept()

#接收信息
mag = conn.recv(1024)
print(mag.decode())
s.close()

