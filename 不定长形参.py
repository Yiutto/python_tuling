# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/5/24.
"""

# 1. 在形参中带* [会将调用函数时溢出位置实参保存成元组的形式，然后赋值*后的变量名]

def foo(x, y, *z):
    print(x)
    print(y)
    print(z)
    print(*z)
print('---------foo----------')
foo(1,2,3,4,5,6,7,8)

# 2.序列类型的实参*打散成位置实参

def zoo(x, y, z):
    print(x, y, z)
print('---------zoo----------')
# 实参打散
zoo(1, *(2,3))
zoo(*(1,2,3))
zoo(*[1,2,3])
zoo(*'abc')
print(1,2,3)
print(*[1,3,2])

# 3.在形参中带**【会将调用函数时溢出关键字实参保存成字典的形式，然后赋值**后的变量名】

def too(x, y, **z):
    print(x)
    print(y)
    print(z)
    # 字典不能这样打散，字典无序，无法独立打散
    # print(**z)
## 错误
# too(1,2,a=1,b=2,c=3,x=1)
# too(1, 2, 3)  # TypeError: too() takes 2 positional arguments but 3 were given
print('---------too----------')
too(1, 2, a=3, b=4)

# 4.字典实参可以打散成关键字实参传参
## 打散字典
## 实参可以打散字典变成关键字实参进行传参
## 为何字典可以打散成关键字，因为字典是无序的，关键字也是无序的
a = {'a': 1, 'b': 2, 'c': 3}
# too(1, 2, a)  # TypeError: too() takes 2 positional arguments but 3 were given
too(1, 2, **a)
too(1, 2, b=3, c=2, a=2)
# 字典独立打散不行
#print(**a)

# 5.不定长参数的规范
## 规范：在形参中带*与**的，*后的变量名应该为args，**后跟的变量名应该为kwargs
## 无敌  可以接受 0 到 无穷个位置参数【*】和关键字参数【**】
def yoo(*args, **kwargs):
    print(args)
    print(kwargs)
print('------yoo------')
yoo()
yoo(1, 2, 3, a=1, b=2)

'''
参数的顺序
  1.形参   位置参数 < 默认参数 < 不定长参数
  2.实参   位置参数 < 关键字参数
'''