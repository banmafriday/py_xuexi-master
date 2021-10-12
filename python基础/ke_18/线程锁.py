# coding:utf-8
import threading

# 线程锁(互斥锁):当一个线程设置上锁之后,必须等锁释放了才能调度其他线程
lock = threading.Lock()  #创建锁

num = 100
def run(name):
    global num
    num=num-1
    lock.acquire()   # 设置锁
    print("线程",name,"执行了",num)
    lock.release()    #释放锁

for i in range(1,101):
    t = threading.Thread(target=run,args = (i,))
    t.start()