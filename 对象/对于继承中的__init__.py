# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/6/7.
"""

class Father:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def print_info(self):
        print(f'父类方法：{self.name}, {self.address}')


class Son(Father):
    # 如果父类中有构造方法那么子类也会使用父类的构造方法
    # 子类定义构造方法之前必须先要运行父类的构造方法
    def __init__(self, name, address, age):
        Father.__init__(self, name, address) # 这个知识点下一节课会细讲
        # super().__init__(self, name, address)
        self.name = name
        self.address = address
        self.age = age

    # 重写父类方法
    def print_info(self):
        print(f'子类方法：{self.name}, {self.address}, {self.age}')

son = Son('yiutto', '抚州', 30)
son.print_info()



