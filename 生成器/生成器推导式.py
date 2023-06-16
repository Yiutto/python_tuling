# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/6/16.
"""

#列表推导式
int_list = [i for i in range(10)]

# 下面不是元组推导式
obj = (i for i in range(10))

print(obj.__next__())
print(obj.__next__())