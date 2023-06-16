# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/6/8.
"""

import threading

class Test(threading.Thread):
    def __init__(self, name, age):
        super().__init__()  # 不加这个会报错  或者 threading.Thread.__init__(self)
        self.name = name
        self.age = age

test = Test('a', 11)

'''
如果父类中存在构造方法，子类也有构造方法
    那么子类在创建构造方法之前必须先要运行父类的构造方法
'''