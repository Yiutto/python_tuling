# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/6/13.
"""

class Dog:
    def bark(self):
        print('狗汪汪叫。。。')


class Hashiqi(Dog):  # 多态（继承和重写）
    def bark(self):
        print('哈士奇在嗷呜的叫。。。')

class ZangAo(Dog):  # 不是多态（只有继承）
    pass

class Person:
    def __init__(self, name):
        self.name = name

    def pk_dog(self, dog):
        print(f'{self.name}正在打来福')
        dog.bark()  # 可以传对象实例

p = Person('yiutto')

h = Hashiqi()
h.bark()

z = ZangAo()
z.bark()

p.pk_dog(h)


