# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/6/16.
"""

# 如果大家在函数中发现关键字yield，函数就不是函数，而是生成器对象。
# 生成器是一种特殊的迭代器
def test(n):
    i = 0
    while i<n:
        yield i
        i += 1

t = test(3)
print(t)
for i in t:
    print(i)

# 生成器研究

def my_range(n):
    print('开始循环取值。。。')
    i = 0

    while i<n:
        print('迭代中。。。。')
        yield i  # 和return关键字类似，可以将结果返回，不会终止，第二次会接着上次执行
        i += 1
        print('迭代结束。。。。')


my_obj = my_range(3)

# 可以对比 前2次next
print(my_obj.__next__())
print(my_obj.__next__())