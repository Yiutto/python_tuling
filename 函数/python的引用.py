# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/6/4.
"""

# 浅拷贝和深拷贝

a = [1, 2]
b = a
print(b)
a.append(3)
print(a)
print(b)


'''
python中的一切皆对象，对象都是引用
'''

def test1():
    print('函数1')

def test2():
    print('函数2')

test1()

test1 = test2  # 没有加小括号的意义是：当前获取的是这个函数的内存地址，并将这个函数的内存地址赋值给test1

test1()


# 匿名函数

def func(a, b, obj):
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'obj = {obj(a, b)}')

# 一个匿名函数可以最为函数参数进行使用
func(1, 2, lambda x, y: x*y)

stus = [
    {'name': 'aaa', 'age': 19},
    {'name': 'bbb', 'age': 99},
    {'name': 'ccc', 'age': 9},
]

stus.sort(key=lambda x: x['age'])
print(stus)