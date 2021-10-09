# coding:utf-8
import time
import pygame
import sys
import random


# 玩家类
# 属性:显示窗口、位置、图片、子弹列表、移动状态
# 方法:显示、移动、开火

class Player():
    def __init__(self, screen):
        self.screen = screen  # 将一个窗口对象作为属性值，表示当前玩家对象的显示窗口
        self.x = 150
        self.y = 500
        self.img = pygame.image.load(r"D:\feiji\he.png")  # 玩家图片
        self.bulLitst = []  # 子弹列表
        self.moveLeftState = 0  # 不移动   1 移动
        self.moveRightState = 0  # 不移动   1 移动

    def display(self):
        self.screen.blit(self.img, (self.x, self.y))  # 显示到窗口

    def move(self):
        pass

    def fire(self):
        pass


# 玩家子弹类


# 属性:显示窗口、位置、图片、
# 方法:显示、移动
class PlayerBullet():
    def __init__(self, screen, x, y):
        self.screen = screen  # 将一个窗口对象作为属性值
        self.x = x  # 子弹初始位置，需要跟随飞机
        self.y = y
        self.img = pygame.image.load(r"D:\feiji\h1.png")  # 玩家图片

    def display(self):
        pass

    def move(self):
        pass


# 敌机类
# 属性:显示窗口、位置、图片、子弹列表、移动状态
# 方法:显示、移动、开火
class Emeny():
    def __init__(self, screen):
        self.screen = screen  # 将一个窗口对象作为属性值，表示当前敌机对象的显示窗口
        self.x = 0
        self.y = 0
        self.img = pygame.image.load(r"D:\feiji\h2.png")  # 玩家图片
        self.bulLitst = []  # 子弹列表
        self.moveState = 1  # 0左移动   1 右移动

    def display(self):
        self.screen.blit(self.img, (self.x, self.y))  # 显示到窗口

    def move(self):
        pass

    def fire(self):
        pass


# 敌机子弹类
# 属性:显示窗口、位置、图片、
# 方法:显示、移动
class EmenyBullet():
    def __init__(self, screen, x, y):
        self.screen = screen  # 将一个窗口对象作为属性值
        self.x = x  # 子弹初始位置，需要跟随敌机
        self.y = y
        self.img = pygame.image.load(r"D:\feiji\h3.png")  # 敌机图片

    def display(self):
        pass

    def move(self):
        pass


# 键盘监控
def key_control(player):
    pass



# main方法

class main():
    screen = pygame.display.set_mode(300, 600)

    # 获取背景
    background = pygame.image.load(r"D:\feiji\bei.png")
    # 创建玩家对象，并传入显示窗口
    player = Player(screen)

    # 创建玩家对象，并传入显示窗口
    emeny = Emeny(screen)

    # 循环显示所有对象并刷新
    while 1 == 1:
        screen.blit(background, (0, 0))
        player.display()  # 对象调用自己的显示方法
        emeny.display()
        pygame.display.update()  # 刷新窗口
        time.sleep(0.05)


if __name__ == "__main__":
    main()
