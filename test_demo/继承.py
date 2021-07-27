# -*- coding: utf-8 -*-
""" 
@Time    : 2021/7/19 14:26
@Author  : MaSai
@FileName: 继承.py
@SoftWare: PyCharm
"""
# class App:
#     def start(self):
#        print('starting')
#
# class Android(App):
#     def getVersion(self):
#        print('Android version')
#
# app = Android()
# app.start()
# app.getVersion()


# class Music:
#     @staticmethod
#     def play():
#         print("*playing music*")
#
# Music.play()
"""
在if 语句中将列表名用在条件表达式中
时，Python将在列表至少包含一个元素时返回True ，并在列表为空时返回False
"""


def s(a):
    if a:
        print('空')
    else:
        print('1')


# s(a="1")


# class A(object):
#     def m1(self, n):
#         print("self:", self)
#
#     @classmethod
#     def m2(cls, n):
#         print("cls:", cls)
#
#     @staticmethod
#     def m3(n):
#         pass
#
# a = A()
# a.m1(1) # self: <__main__.A object at 0x000001E596E41A90>
# A.m2(1) # cls: <class '__main__.A'>
# A.m3(1)
# class MyClass:
#         name = 'FishC'
#
#         def myFun(self):
#             print("Hello FishC!")
#
# # MyClass.name
# a= MyClass()
# a.myFun()
# 按照以下要求定义一个游乐园门票的类，并尝试计算2个成人+1个小孩平日票价
# 平日票价100元
# 周末票价为平日的120%
# 儿童半票

class Park:
    def money(self, week, person, child):
        price = 100
        """week
        0：周一到周五
        1：周末
        """
        if week == 0:
            reslut = person * price + (child * price * 1 / 2)
        elif week == 1:
            reslut = (person * price * 1.2) + (child * price * 1 / 2 * 1.2)
            pass
        return reslut

# park=Park()
# print(park.money(0, 2, 1))
# print(park.money(1, 2, 1))

# import random as r
#
# legal_x = [0, 10]
# legal_y = [0, 10]
#
#
# class Turtle:
#     def __init__(self):
#         # 初始体力
#         self.power = 100
#         # 初始位置随机
#         self.x = r.randint(legal_x[0], legal_x[1])
#         self.y = r.randint(legal_y[0], legal_y[1])
#
#     def move(self):
#         # 随机计算方向并移动到新的位置（x, y）
#         new_x = self.x + r.choice([1, 2, -1, -2])
#         new_y = self.y + r.choice([1, 2, -1, -2])
#         # 检查移动后是否超出场景x轴边界
#         if new_x < legal_x[0]:
#             self.x = legal_x[0] - (new_x - legal_x[0])
#         elif new_x > legal_x[1]:
#             self.x = legal_x[1] - (new_x - legal_x[1])
#         else:
#             self.x = new_x
#         # 检查移动后是否超出场景y轴边界
#         if new_y < legal_y[0]:
#             self.y = legal_y[0] - (new_y - legal_y[0])
#         elif new_y > legal_y[1]:
#             self.y = legal_y[1] - (new_y - legal_y[1])
#         else:
#             self.y = new_y
#             # 体力消耗
#         self.power -= 1
#         # 返回移动后的新位置
#         return (self.x, self.y)
#
#     def eat(self):
#         self.power += 20
#         if self.power > 100:
#             self.power = 100
#
#
# class Fish:
#     def __init__(self):
#         self.x = r.randint(legal_x[0], legal_x[1])
#         self.y = r.randint(legal_y[0], legal_y[1])
#
#     def move(self):
#         # 随机计算方向并移动到新的位置（x, y）
#         new_x = self.x + r.choice([1, -1])
#         new_y = self.y + r.choice([1, -1])
#         # 检查移动后是否超出场景x轴边界
#         if new_x < legal_x[0]:
#             self.x = legal_x[0] - (new_x - legal_x[0])
#         elif new_x > legal_x[1]:
#             self.x = legal_x[1] - (new_x - legal_x[1])
#         else:
#             self.x = new_x
#         # 检查移动后是否超出场景y轴边界
#         if new_y < legal_y[0]:
#             self.y = legal_y[0] - (new_y - legal_y[0])
#         elif new_y > legal_y[1]:
#             self.y = legal_y[1] - (new_y - legal_y[1])
#         else:
#             self.y = new_y
#         # 返回移动后的新位置
#         return (self.x, self.y)
#
#
# turtle = Turtle()
# fish = []
# for i in range(10):
#     new_fish = Fish()
#     fish.append(new_fish)
#
# while True:
#     if not len(fish):
#         print("鱼儿都吃完了，游戏结束！")
#         break
#     if not turtle.power:
#         print("乌龟体力耗尽，挂掉了！")
#         break
#
#     pos = turtle.move()
#     # 在迭代器中删除列表元素是非常危险的，经常会出现意想不到的问题，因为迭代器是直接引用列表的数据进行引用
#     # 这里我们把列表拷贝给迭代器，然后对原列表进行删除操作就不会有问题了^_^
#     for each_fish in fish[:]:
#         if each_fish.move() == pos:
#             # 鱼儿被吃掉了
#             turtle.eat()
#             fish.remove(each_fish)
#             print("有一条鱼儿被吃掉了...")
# class MyClass:
#     def __init__(self):
#         return "I love FishC.com!"

# class A:
#     def s(self):
#         print("A")
# class B(A):
#     def s(self):
#         print("B")
#
#
# a=A()
# a.s()
# b=B()
# b.s()
# a.s()


class A():
    def __init__(self):
        print("进入A…")
        print("离开A…")


class B(A):
    def __init__(self):
        print("进入B…")
        super().__init__()
        print("离开B…")


class C(A):
    def __init__(self):
        print("进入C…")
        super().__init__()
        print("离开C…")


class D(B, C):
    def __init__(self):
        print("进入D…")
        super().__init__()
        super().__init__()
        print("离开D…")
D()