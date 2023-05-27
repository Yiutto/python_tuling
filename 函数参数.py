# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/5/24.
"""

# 1. 无参数
def factory():
    print('正在造飞机')
factory()

# 2. 有参数

## 2.1 形参
'''
 a.对于大多数情况下传的值都不相同，应该定义为位置形参
 b.对于大多数情况下传的值相同，应该定义为默认形参
 c. 位置形参应该放到默认形参前面
'''

### 2.1.1 位置形参
def factory(a, b):
    print('a是%s' % a)
    print('b是%s' % b)

### 2.1.2 默认形参

def factory1(a, b=3):
    print(a)
    print(b)

factory1(1, 6)
## 2.2 实参
'''
 a.位置实参必须放到关键字时长前面
 b.不能对一个形参重复赋值
'''

### 2.2.1 位置实参
factory(3, 2)
# 错误示范
#factory(3, 2, 1)
#factory(1)

### 2.2.1 关键字实参
factory(a=1, b=2)
factory(b=1, a=2)
factory(1, b=2)
print('-----')
factory(**{'a': 25, 'b': 250})

# 错误示范
# factory(a=1,a=3)
# factory(a=1,2)
# factory(1, a=3)
