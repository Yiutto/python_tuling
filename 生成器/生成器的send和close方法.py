# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/6/16.
"""
'''
1.当代码运行到yield会保存状态并暂停
2.yield可以和return一样返回数据
3.可以接收send发送过来的数据

yield后面的变量会被直接返回
yield前面的赋值语句会将接收到的信息赋值给yield前面的变量
'''

def my_range(n):
    i = 0
    while i<n:
        value = yield i
        print(value)
        i += 1

# 1.创建生成器对象
obj = my_range(3)

# 对比下面2次运行的变化
print(obj.__next__())
print(obj.__next__())


# 通过send方法驱动生成器函数
# send方法可以向生成器函数传递自定义数据的
# send方法“不能”在next方法之前运行
print(obj.send('sssss'))