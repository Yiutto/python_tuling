# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/6/6.
"""

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def print_info(self):
        print(f'我叫{self.name}，今年{self.age}岁')

tom = Cat('TOM', 3)
tom.print_info()
tom.age = -10
tom.print_info()

class Teacher:
    def __init__(self):
        self.name = 'yiutto'
        self.__age = 30

    def set_age(self, new_age):
        if 1<=new_age<=120:
            self.__age = new_age
            print('年龄设置成功')
        else:
            print('年龄设置数据有误。。')

    def get_age(self):
        return self.__age

t = Teacher()
print(t.name)
print(t.get_age())
t.set_age(100)
print(t.get_age())
