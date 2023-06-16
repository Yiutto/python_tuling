# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/6/13.
"""

class Father:
    def print_info_1(self):
        print('实例方法')

    @staticmethod
    def print_info_2():
        print('静态方法')

    @classmethod
    def print_info_3(cls):
        print('类方法')

f = Father()

print(f.__class__)
f.print_info_1()
f.print_info_2()
f.print_info_3()

print('--------')

# __class__可以省略
f.__class__.print_info_1(f)
f.__class__.print_info_2()
f.__class__.print_info_3()

# 如果大家想知道一个实例对象有多少属性和方法
# 可以使用一个内置函数

print(dir(f))

'''
__init__
__str__
__class__

类对象无法访问实例属性
    实例属性保存在实例对象中的
    
    实例对象和类对象是隔离状态
'''