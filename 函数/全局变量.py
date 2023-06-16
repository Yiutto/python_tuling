# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/6/4.
"""

num = 10


def add_num():
    global num  # 当对象为不可变类型时，需要添加global
    num += 1
    return num


print(add_num())


L = [1, 3, 4]


def add_list():
    L.append(2)  # 当对象为可变类型时，不需要添加global
    return L


print(add_list())