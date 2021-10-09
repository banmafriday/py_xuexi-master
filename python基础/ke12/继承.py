# coding:utf-8
# 类的继承

class Animal():

    def __init__(self, color, age):
        print("Animal初始化方法被调用!")
        self.color = color
        self.age = age

    def eat(self):
        print("动物在吃!")

    def run(self):
        print("动物在跑!")


class Cat(Animal):
    pass


class Dog():
    pass


class Bird():
    def fly(self):
        print("鸟在飞!!!")


# --------------
c1 = Cat("橘色", 18)
c1.eat()

b2 = Bird()
b2.fly()
