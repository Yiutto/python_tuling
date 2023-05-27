# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/5/24.
"""
# 九九乘法表
for i in range(1, 10):
    # print('i=%d' % i)
    # print("-----------")
    for j in range(1, i+1):
        print('{} * {} = {} '.format(i, j, i*j), end=' ')
    print(end='\n')
