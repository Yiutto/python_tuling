# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/6/4.
"""


def test(a, b, c=100, d=200):
    print(f'a={a}, b={b}, c={c}, d={d}')


test(11, 12)
test(11, 12, 33)
test(11, 12, 33, 44)
test(111, 221, c=333, d=444)
test(c=0, b=-2, a=1, d=3)


# test(c=0, d=1, 11, 12)  # 函数命名参数的传递方式不能在默认传递方式的前面
# test(c=1, d=2)  # 如果只传递默认参数的值，报错，  因为形参拿不到值
# test(1, 2, a=3, d=4)  错误

