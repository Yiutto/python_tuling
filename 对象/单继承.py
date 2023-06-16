# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/6/7.
"""

'''
父类必须要遵守通用型这一原则
    父类可以被无数个子类继承
    
如果想要对父类添加新功能
    必须在子类中添加，不要强行修改父类代码
'''

class Animal:
    def run(self):
        print('跑步')

    def eat(self):
        print('吃饭')

    def sing(self):
        print('唱歌')

    # def info(self):  #  强烈不建议这样写，因为父类根本没有 name,age属性【不要为了偏爱Dog而让其他子类难受】
    #     print(self.name, self.age)

class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 如果需要添加新功能，必须在子类中，如果将新功能写入到父类，会影响到所有的子类
    def info(self):
        print(self.name, self.age)


dog = Dog('yiutto', 30)
dog.eat()
dog.run()
dog.sing()
dog.info()





