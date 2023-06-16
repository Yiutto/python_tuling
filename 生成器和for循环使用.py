# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/6/1.
"""

'''
总结yield：只能在函数内使用
    1.yield提供了一种自定义迭代器的解决方案
    2.yield可以保存函数的暂停的状态
    3.yield对比return
        1.相同：都可以返回值，值的类型个数都没有限制
        2.不同：yield可以返回多次值【暂停】，而return只能返回一次值函数就结束了【结束】
'''

'''
定义一个生成器，这个生成器可以生成10位斐波那契数列
    ：数列中每一个数的值都等于前2个数相加的值[0, 1,1,2,3,5,8,13,21,...]
'''
def run(n):
    i, a, b = 0, 0, 1
    while i<n:
        yield a   # a第一是 a 1 b 1   第二次 a 1 b 2 第三次 a 2 b 3  第四次 a 3 b 5 第五次 a 5 b 8
        print(a)
        a, b = b, a+b
        i += 1
my_run = run(10)
print(my_run)

print(list(my_run))


def run(n):
    i, a, b = 0, 0, 1
    while i<n:
        yield a   # a第一是 a 1 b 1   第二次 a 1 b 2 第三次 a 2 b 3  第四次 a 3 b 5 第五次 a 5 b 8
        b, a = a+b, b
        i += 1
my_run = run(10)

print(list(my_run))


# 用中间变量进行处理
def run1(n):
    i = 0
    a = 0
    b = 1

    while i < n:
        yield a
        tmp = a + b  # 将 前后2个数字相加赋值到tmp变量
        a = b   # 将b的值赋值给 变量a
        b = tmp   # 将tmp值赋值给 变量b
        i += 1
print(list(run1(10)))


# 用列表保存
def run2(n):
    L = []
    i = 0
    a = 0
    b = 1

    while i < n:
        L.append(a)
        tmp = a + b  # 将 前后2个数字相加赋值到tmp变量
        a = b   # 将b的值赋值给 变量a
        b = tmp   # 将tmp值赋值给 变量b
        i += 1
    return L
print(run2(10))


