# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/6/4.
"""

int_set = {1, 2, 3, 4}
print(type(int_set))

# 添加单个元素
int_set.add('a')
print(int_set)

# update 传递 str list tuple set dict
int_set.update('abc')
print(int_set)

int_set.update({'name': 'yiutto', 'age': 18})
print(int_set)

