# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/6/1.
"""

info = {'name': '翠花', 'age': 18, 'sex': 'man', 'address': '北京'}

# info.pop('age')
# x = info.__iter__()
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
#
#
# print('-------------')
# print(info.__iter__().__next__())
# print(info.__iter__().__next__())
# y = info.__iter__().__iter__()
# print('##################')
# print(y.__next__())
# print(y.__next__())
# print(y.__next__())

s = iter(info)
# print(s)
# print(s.__iter__())
# print(s.__next__())
# print(s.__next__())
# print(s is s.__iter__().__iter__())
# while True:
#     try:
#         print(next(s))
#     except StopIteration:
#         print('已经全部输出')
#         break
#
# print('==================')
# while True:
#     try:
#         print(s.__next__())
#     except StopIteration:
#         print('over')
#         break

# obj_iter 可迭代对象
obj_iter = range(1,10)
print(obj_iter)

# obj_next为迭代器
obj_next = obj_iter.__iter__()

for i in obj_next:
    print(i)
print('再次')
for i in obj_next:
    print(i)
print('------------')
for i in obj_iter:
    print(i)
print('再次')
for i in obj_iter:
    print(i)

# obj_iter迭代对象会生成新的迭代器
# obj_next是基于老的迭代器取值


