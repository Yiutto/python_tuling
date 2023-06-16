# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/6/4.
"""

'''
给函数传递一个容器类型并进行拆包 列表、元组、集合
'''
def test2(a, b, c):
    print(a + b + c)


nums = [1, 2, 3]
# 如果一个函数中的参数需要根据一个容器进行拆包赋值
# 当前容器类型元素个数以参数个数一致的情况下才能使用 * 号拆包
test2(*nums)

# *不能拆字典，只能拆字典的key， 用** 可以拆字典
def test3(name, age, address):
    print(name, age, address)

info = {
    'name': 'yiutto',
    'age': 30,
    'address': '深圳'
}

test3(**info)


'''
不定长参数在声明可以使用*/**
在函数调用传递参数的时候可以使用 *、**
** 拆字典
打印的时候不能添加*
'''
def test(*args, **kwargs):
    # print(args, kwargs)  # 粗错误
    print(args, kwargs)

# 如果一个函数中有一个单独的*，那么在这个单独的* 后面的参数必须使用命名参数
def test_2(a, *, b=2, c=3):
    print(a, b, c)

# 为了保证参数传递不出错 使用单独的*对其后面的参数强制使用命名参数传递

# test_2(1, 2, 3)  # 报错
test_2(1, b=4, c=5)
