# coding:utf-8
# 多进程:一个程序运行过程中,产生了多个进程

# 如果现在有n个正在运行的程序对应的至少N个进程

# 引入进程类
from  multiprocessing import Process

import time

def run1():
    print("任务执行了!")
    time.sleep(5)

def run2():
    print("任务执行了!")
    time.sleep(5)

def run3():
    print("任务执行了!")
    time.sleep(5)

#创建进程对象
p1 = Process(target=run1())   #target=run1  要执行的任务方法
p2 = Process(target=run2())   #target=run1  要执行的任务方法
p3 = Process(target=run3())   #target=run1  要执行的任务方法

if __name__=="__main__":   #启动程序只能写到mian中
    p1.start()   #启动进程
    p2.start()
    p3.start()