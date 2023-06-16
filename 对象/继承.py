# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/6/7.
"""

# 继承
'''
1.子类【派生类】在继承父类【基类】的时候，需要在括号内写父类的名字
父类可以有多个子类


'''
class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass


'''
子类可以获取父类中的所有方法和属性，
   私有属性和私有方法也是可以继承，但需要通过接口进行封装
'''
class A:
    def __init__(self):
        self.num = 3
        self.__age = 19  # 私有属性变量

    def get_num(self):
        print(self.num)

    def __get_age(self):  # 私有方法，不能直接被子类所访问
        print(self.__age)

    def get_age(self):   # 封装私有方法调用接口，可以被子类所访问
        self.__get_age()


class B(A):
    pass

b = B()
print(b.num)
b.get_num()
# print(b.__age)  不能调用
# b.__get_age()   不能调用
b.get_age()

print(dir(A))
print(dir(B))


#b._A__get_age()  # 该方法千万不能在项目中使用