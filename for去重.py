# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/5/24.
"""

info = [
    {'name': 'dahai', 'age': 18},
    {'name': 'xialuo', 'age': 78},
    {'name': 'xishi', 'age': 8},
    {'name': 'dahai', 'age': 18},
    {'name': 'dahai', 'age': 18}
]

# 不行
# print(set(info))

L = []
for i in info:
    if i not in L:
        L.append(i)

print(L)