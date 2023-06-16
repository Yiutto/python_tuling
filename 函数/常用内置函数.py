# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/5/29.
"""

# 绝对值
print(abs(-5))
print('----\n')
# all(可迭代对象) 很像 and
# 返回的是布尔值
## 可迭代对象里面的值全为真才是真，其他为假
## 可迭代对象是空则为真 ????
print(all([1, '', None]))
print(all([1, 'aa', 2]))
print(all([]))
print('----\n')

# any(可迭代对象) 很像or
## 可迭代对象里面的值全部为假才是假，其余为真
## 可迭代对象为空则为假

print(any([1, '', None]))
print(any([1, 'aa', 2]))
print(any([]))
print('----\n')

# 聚合函数
## 最大
print(max([1, 2, 3, 4, 5]))
print('----\n')
## 最小
print(min([1, 2, 3, 4, 5]))
print('----\n')
## 求和
print(sum([1, 2, 3]))
print('----\n')

# asilll码
## 字符转成编码
print(ord('a'))
## 编码转字符
print(chr(98))
print('----\n')

# 拉链函数 zip
t1 = ['a', 'b', 'c', 'd', 'e'] # e被舍弃
t2 = [1, 2, 3, 4]

print(list(zip(t1, t2)))
print(dict(zip(t1, t2)))

# exec函数 可以执行字符串里面的代码，支持python语法
exec('print(1,2)')
exec('''
for i in range(0, 10):
    for j in range(1, i+1):
        print('%d * %d = %d' % (i, j, i*j))
''')
