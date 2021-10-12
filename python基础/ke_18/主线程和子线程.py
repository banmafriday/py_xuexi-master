# coding:utf-8
#创建多线程
import threading
import time

def run(name):
    time.sleep(5)
    print("任务执行了!")
#程序执行时,程序本身就是一个线程,称为主线程
# 主线程执行过程中不会等待子线程执行完毕,会直接执行后面的代码

# 创建线程子对象
t1 = threading.Thread(target=run,args = ("t1",))
t2 = threading.Thread(target=run,args = ("t2",))
t3 = threading.Thread(target=run,args = ("t3",))

#启动线程
t1.start()
t2.start()
t3.start()

t1.join()    #需要等待当前线程执行完毕,才能继续执行主线程
t2.join()    #需要等待当前线程执行完毕,才能继续执行主线程
t3.join()    #需要等待当前线程执行完毕,才能继续执行主线程


print("执行完毕!")