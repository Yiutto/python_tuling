# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/6/13.
"""

class Father:
    def __init__(self, name):
        self.name = name

    # 当方法无需使用实例属性时，将实例方法转为静态方法
    @staticmethod
    def print_info(): # 将一个函数归类到某个类中，必须经过这个类才能调用，  调用权限
        print('我是一个方法')

f = Father('yiutto')
f.print_info()

Father.print_info()
'''
在类中的方法上使用@staticmethod特殊语法对方法进行装饰的话
    则这个方法会转换为静态方法
    
        无需使用类中的属性这种情况就可以
        
    调用： 1.实例对象
          2.类对象
'''