# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/6/5.
"""


class Hero(object):

    def info(self):
        '''
        当对象调用实例方法时，python会自动将对象本身的引用作为参数，传递到实例方法的第一个参数self里面
        :return:
        '''
        print(self)
        print("self各不同，对象是出处")


# 创建一个对象
h1 = Hero()

h1.info()
print('---------------------')
print(h1)
print(id(h1))


class Hero1(object):

    def set_info(self):
        self.name = '安娜'
        self.age = 19
        self.address = '长沙'

    def print_info(self):
        print(self.qq, self.email)

hero1 = Hero1()
hero1.set_info()  # 这段代码必须执行，否则报错，该方法不调用其定义的属性就不会执行。
print(hero1.name, hero1.age, hero1.address)

print('---' * 20)


class Hero2(object):
    def set_info(self):
        pass


hero2 = Hero2()
hero2.name = 'lle'
hero2.age = 18
print(hero2)
print(hero2.age)
print(hero2.name)

print('---' * 20)

class Hero3(object):
    def set_info(self):
        self.name = 'liudehua'
        self.age = 60

    def print_info(self):
        print(self.qq, self.email)

hero3 = Hero3()
hero3.set_info()
print(hero3.name, hero3.age)
hero3.qq = '1102390'
hero3.email = 'yiutto@qq.com'
hero3.print_info()
hero3.name = 'zhangxueyou'
hero3.age = 70
print(hero3.name, hero3.age)

print('---' * 20)


class Cat(object):

    def set_info(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('%s 正在吃鱼' % self.name)

    def drink(self):
        print('%s 正在喝可乐' % self.name)

    def print_info(self):
        print('名字是 %s，年龄是 %d' % (self.name, self.age))

tom = Cat()

# 通过类对象调用实例
Cat.set_info(tom, '小黑', 3)

Cat.eat(tom)
Cat.drink(tom)
Cat.print_info(tom)