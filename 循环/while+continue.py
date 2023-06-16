# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/5/24.
"""
# while + continue: continue 代表结算本次循环
# （本次循环continue之后的代码不在运行），直接进入下次循环

# start = 0
# while start < 8:
#     start += 1
#     if start == 4:
#         continue
#     print(start)

i = 1
j = 1
while i < 10 and j < 20:
    i += 1
    j += 3
    if i == 3:
        continue
    if j % 2 == 1:
        print('j：{} 为奇数'.format(j))
        if i > 5:
            print('i: {} 大于5'.format(i))
            continue

    print('i: {}'.format(i))
    print('j: {}'.format(j))