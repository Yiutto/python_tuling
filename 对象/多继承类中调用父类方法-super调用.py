# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/6/14.
"""

class Parent:
    def __init__(self, name, *args, **kwargs):  # 为避免多继承报错，使用不定长参数，接受参数
        print('parent的init开始被调用')
        self.name = name
        print('parent的init结束调用')


class Son1(Parent):
    def __init__(self, name, age, *args, **kwargs):  # 为避免多继承报错，使用不定长参数，接受参数
        print('Son1的init开始被调用')
        self.age = age
        super().__init__(name, *args, **kwargs)
        print('Son1的init结束调用')

class Son2(Parent):
    def __init__(self, name, gender,  *args, **kwargs):
        print('Son2的init开始被调用')
        self.gender = gender
        super().__init__(name, *args, **kwargs)
        print('Son2的init结束调用')

# class Son2():   # 前是先从左边开始搜索 调用son1 在son1中存在super函数 会调用son1的super并检查是否存在共同继承的子类 这个地方son2没有继承 所以走Parent 走到Parent之后已经是顶级类了   代码结束   son2永远无法被调用
#     def __init__(self, name, gender, *args, **kwargs):
#         print('Son2的init开始被调用')
#         self.gender = gender
#         print('Son2的init结束调用')

class Grandson(Son1, Son2):
    def __init__(self, name, age, gender):
        print('Grandson的init开始被调用')
        # 多继承时，相对于使用类名.__init__方法，要把每个父类全部写一遍
        # 而super只用一句话，执行了全部父类的方法，这也是为何多继承需要全部传参的一个原因
        # super(Grandson, self).__init__(name, age, gender)
        #super().__init__(name, gender, age)  # 这里顺序不同，得到结果会发生变化， 最后在定义构造方法 添加一个 * ，如 def __init__(self, *, name, age, gender)
        super().__init__(name, age, gender)
        # Son2.__init__(self, name, gender)
        print('Grandson的init结束被调用')

gs = Grandson('grandson', 12, '男')
print('姓名：', gs.name)
print('年龄：', gs.age)
print('性别：', gs.gender)
print('*****多继承使用super().__init__发生的状态*****\n')


'''
super在多继承中依次执行父类中的方法
如果去确定执行顺序  mro是方法  所以在类对象

1.super可以调用父类方法
2.可以防止多重调用
3.可以检测父类汇总所需要的的属性并进行传递，传递一个少一个
'''
print(Grandson.__mro__)