# pygame游戏开发
# 二维游戏开发(动画)
import pygame
import sys
import time
from pygame.locals import *  # 检测事件

# 创建窗口
screen = pygame.display.set_mode((1254, 386))

# 读取图片
img1 = pygame.image.load(r"C:\\Users\\banma\\Desktop\\1.jpg")  # 背景
img2 = pygame.image.load("C:\\Users\\banma\\Desktop\\22.jpg")  # 飞机

while 1 == 1:
    a = 10  # x轴位置
    b = 100  # y轴位置

    for i in range(60):
        # 在窗口加入对象
        screen.blit(img1, (0, 0))

        screen.blit(img2, (a, b))

        # 刷新窗口,显示所有对象
        pygame.display.update()
        if i <= 30:

            a += 10  # 向右移动10个像素
        else:
            a -= 10  # 向左移动10个像素
        time.sleep(0.1)

        for event in pygame.event.get():  # 获取所有用例事件
            if event.type == QUIT:  # 退出
                print("正在退出")
                sys.exit()
