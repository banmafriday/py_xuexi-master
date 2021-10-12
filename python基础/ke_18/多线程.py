# coding:utf-8
#创建多线程
import threading
import time

def run(name):
    print("任务执行了!")
    time.sleep(5)

# 创建线程对象
t1 = threading.Thread(target=run,args = ("t1",))
t2 = threading.Thread(target=run,args = ("t2",))
t3 = threading.Thread(target=run,args = ("t3",))

#启动线程
t1.start()
t2.start()
t3.start()

#多进程切换小号的cpu资源较多!