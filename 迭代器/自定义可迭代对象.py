# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/6/15.
"""

from collections.abc import Iterable

class Test:
    def __init__(self):
        self.list_obj = []

    # 如果一个类实现__iter__方法，那么它一定是可迭代对象
    def __iter__(self):
        pass

    def add(self, item):
        self.list_obj.append(item)


test = Test()
test.add(1)
test.add(2)
test.add(3)

print(isinstance(test, Iterable))