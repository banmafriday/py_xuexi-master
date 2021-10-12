# coding:utf-8
# 客户端发消息给服务端
from socket import *

#创建socket对象
# AF_INET
# AF_UNIX 本机通信,AF_INET(IPV4),AF_INET6
# SCCK_STREAM(TCP)   SOCK_DGRAM(UDP)
s =socket(AF_INET,SOCK_DGRAM)

#和目标建立连接

s.connect(("localhost",6363))

# 发送消息
s.send("你好!服务端".encode())

#关闭socket
s.close()