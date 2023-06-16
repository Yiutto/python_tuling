# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/5/29.
"""

# L = [1, 2, 3, 4]
# n = L.pop()
#
# print(L)
# print(n)
#
# meiyou=L.append(5)
#
# print(L)
# print(meiyou)


'''
# 无类型限制
def factory(a):
    c = a + 1
    print(c)
    def inner():
        print('factory里面的函数')
    return  'adsdsad'
    return c
    return  inner
b = factory(1)
print(b)

# 无个数限制
def factory(a):
    c = a + 1
    return [1, 23, 4], True, 4, 'adsdsad', c

b = factory(1)
print(b)
print(type(b))
'''

def factory(a):
    print("=====")
    print("=====")
    print("=====")
    while True:
        while True:
            while True:
                if a == 3:
                    return
                a += 1
                print(a)

factory(1)
