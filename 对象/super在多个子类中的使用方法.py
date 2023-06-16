# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/6/12.
"""

class Father:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 特殊的方法 魔术方法
    # python自己实现的一些方法被称之为魔术方法
    # 如果使用print打印一个类的实例对象本身  则会自动触发 __str__ 方法
    def __str__(self):
        return f'{self.name}的年龄是：{self.age}'

class Son(Father):
    def __init__(self, name, age, address):  # 在子类中运行父类的 构造方法，不需要手动去创建父类已经存在的属性。
        super().__init__(name, age)
        self.address = address

    def __str__(self):
        return f'{self.name}的年龄是：{self.age}, 住在 {self.address}'

class GrandSon(Son):
    def __init__(self, *args, **kwargs):
        # 调用父类的构造方法
        # 在当前这个父类中存在多个实例属性，可以试用不定长参数接收
        super().__init__(*args, **kwargs)
        print('这里可以创建一些其他的实例属性。。。')

f = Father('父亲', 50)
print(f)

s = Son('儿子', 20, '南昌')
print(s)

g = GrandSon('孙子', 5, '南京')
print(g) # 这里会调用Son的__str__
