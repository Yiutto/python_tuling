# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/6/15.
"""

# 实现__iter__和__next__方法，获取迭代器

from collections.abc import Iterable, Iterator

class MyList:
    def __init__(self):
        self.list_obj = list()

    # 如果一个类实现__iter__方法，那么它一定是可迭代对象
    def __iter__(self):
        my_iterator = MyIterator(self)
        return my_iterator

    def add(self, item):
        self.list_obj.append(item)

class MyIterator:
    def __init__(self, my_list):    # my_list 接收的是Mylist的实例对象
        self.my_list = my_list
        # 计数器
        self.current = 0

    def __iter__(self):
        return self  # 当前迭代器类自身就是一个迭代器，所以返回这个类本身实例就可以

    # 手动实现迭代规则
    def __next__(self):
        if self.current < len(self.my_list.list_obj):
            item = self.my_list.list_obj[self.current]
            # 获取到列表元素后+1
            self.current += 1
            return item
        else:
            # 手动抛出异常
            # 因为for循环如果接这个异常就会自动break
            raise StopIteration

mylist = MyList()

for i in range(5):
    mylist.add(i)

for item in mylist:
    print(item)