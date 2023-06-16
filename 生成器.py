# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/6/1.
"""

def func():
    print('======1')
    yield 1
    print('------2')
    yield 2
g = func()

print('测试')
print(g is g.__iter__().__iter__())
# print(g.__next__())
# 会触发函数执行，直到碰到一个yield停下来，并将yield后的值当做本次next结果返回
res1 = next(g)
print(res1)
res2 = g.__next__()
print(res2)
