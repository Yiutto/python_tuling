# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/6/15.
"""

nums = [1, 2, 3, 4]
# 获取迭代器
iter_obj = iter(nums)

while True:
    try:
        print(next(iter_obj))
    except StopIteration:
        break


'''
1.迭代对象转为迭代器
2.创建一个死循环调用next方法
3.通过异常处理 结束循环

在 for循环底层也用到了迭代器
'''
for i in nums:
    print(i)