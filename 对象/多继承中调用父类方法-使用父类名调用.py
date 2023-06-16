# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/6/14.
"""

class Parent:
    def __init__(self, name):
        print('parent的init开始被调用')
        self.name = name
        print('parent的init结束调用')

class Son1(Parent):
    def __init__(self, name, age):
        print('Son1的init开始被调用')
        self.age = age
        Parent.__init__(self, name)  # 通过父类名进行调用
        print('Son1的init结束调用')

class Son2(Parent):
    def __init__(self, name, gender):
        print('Son2的init开始被调用')
        self.gender = gender
        Parent.__init__(self, name)  # 通过父类名进行调用父类的构造函数
        print('Son2的init结束调用')

class Grandson(Son1, Son2):
    def __init__(self, name, age, gender):
        print('Grandson的init开始被调用')
        Son1.__init__(self, name, age)   # 单独调用父类的初始化方法
        Son2.__init__(self, name, gender)
        print('Grandson的init结束被调用')

gs = Grandson('grandson', 12, '男')
print('姓名：', gs.name)
print('年龄：', gs.age)
print('性别：', gs.gender)

print("*******多继承使用类名.__init__发生的状态*******\n\n")