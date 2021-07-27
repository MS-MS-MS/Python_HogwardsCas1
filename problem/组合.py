# -*- coding: utf-8 -*-
""" 
@Time    : 2021/7/26 15:23
@Author  : MaSai
@FileName: 组合.py
@SoftWare: PyCharm
"""

"""
0. 思考这一讲我学习的内容，请动手在一个类中定义一个变量，用于跟踪该类有多少个实例被创建（当实例化一个对象，这个变量+1，当销毁一个对象，这个变量自动-1）。fY.|5m

"""


class A:
    count = 0

    def __init__(self):
        A.count += 1

    def __del__(self):
        A.count -= 1


# a=A()
# a1=A()
# a2=A()
# print(A.count)
# del a
# print(A.count)


# class C:
#     def x(self):
#         print('Xman')
# c=C()
# c.x()
# c.x=1
# c.x()
class C:
    def __init__(self, size=10):
        self.size = size

    def getSize(self):
        return self.size

    def setSize(self, value):
        self.size = value

    def delSize(self):
        del self.size

    x = property(getSize, setSize, delSize)


# c=C()
# print(c.x)
# print(c.getSize)
# print(c.size)
# c.size=20
# print(c.size)

class A:
    pass


class B(A):
    pass


# 判断B是不是A的子类 B是否继承A
# print(issubclass(B, A))

b1 = B()


# 判断b1 是不是B的实例对象
# print(isinstance(b1, B))
# print(isinstance(b1, A))
# print(isinstance(b1, C))
# print(isinstance(b1, (A, B, C)))


class CC:
    def __init__(self, x=0):
        self.x = x


# cc1=CC()
# hasattr 判断 cc1 是否存 x对象
# print(hasattr(cc1, 'x'))
# # getattr
# print(getattr(cc1, "x"))
# print(getattr(cc1, "x","找不到"))

# setattr 设置对象中指定属性的值 如果指定属性不存在,则新建一个新的属性属性的值
# print(setattr(cc1,'y','x'))
# delattr 删除对象指定属性的值
# print(delattr(cc1, 'x'))
# print(delattr(cc1, 'x'))


# x

# class CapStr(str):
#     def __new__(cls, string):
#         string= string.upper()
#         return str.__new__(cls,string)
#
# a =CapStr("I Love Fishc.com!")
# print(a)

# class Foo:
#     def foo(self):
#         self.foo = "I love FishC.com!"
#         return self.foo
#
# foo = Foo()
# print(foo.foo())
# 'I love FishC.com!'


# def calc(a, b, c):
#     return (a + b) * c
#
# a = calc(1, 2, 3)
# b = calc([1, 2, 3], [4, 5, 6], 2)
# c = calc('love', 'FishC', 3)
# print(a)
# # 9
# print(b)
# # [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
# print(c)
# loveFishCloveFishCloveFishC

# class NewInt(int):
#     def __add__(self, other):
#         return int.__add__(self,other)
#
#     def __sub__(self, other):
#         return int.__sub__(self,other)
#
# a=NewInt(3)
# b=NewInt(5)
# c=2
# print(a+c)
# print(a+5)
# print(a + b)

# class Try_int(int):
#     def __add__(self, other):
#         return self+other
#
#     def __sub__(self, other):
#         return self-other
#
# a= Try_int(3)
# b= Try_int(5)
# print(a + b)


class Nint(int):
    def __radd__(self, other):
        return int.__sub__(self, other)


# a = Nint(5)
# b = Nint(3)
# # print(a + b)
# # 1+a  1没有定义"+" 就去找a，a定义了 Nint下的 radd  a=self 1=other
# # print(int(1)+a)
# # print(int(1)+2)
# print(a + 1)


class C:
    def __init__(self, *args):
        if not args:
            print("请传入参数")
        else:
            print("参数的个数是%s" % len(args))
            for num in args:
                print(num, end=" ")


# class C:
#     def __init__(self, *args):
#         if not args:
#             print("并没有传入参数")
#         else:
#          print("传入了 %d 个参数，分别是：" % len(args), end='')
#          for each in args:
#             print(each, end=' ')


c = C()
c = C(1, 2, 3)

# class CC:
#     count=0
#     def __init__(self):
#         CC.count=CC.count+1
#
#     def get_count(self,a):
#         CC.count= CC.count+a
#         return CC.count
#
# cc =CC()
# print(cc.count)
# print(cc.get_count(2))


class Word(str):
    '''存储单词的类，定义比较单词的几种方法'''

    def __new__(cls, word):
        # 注意我们必须要用到 __new__ 方法，因为 str 是不可变类型
        # 所以我们必须在创建的时候将它初始化
        if ' ' in word:
            print ("Value contains spaces. Truncating to first space.")
            word = word[:word.index(' ')] #单词是第一个空格之前的所有字符
        return str.__new__(cls, word)

    def __gt__(self, other):
        return len(self) > len(other)
    def __lt__(self, other):
        return len(self) < len(other)
    def __ge__(self, other):
        return len(self) >= len(other)
    def __le__(self, other):
        return len(self) <= len(other)
'FishC'>Word('FisXXhC')