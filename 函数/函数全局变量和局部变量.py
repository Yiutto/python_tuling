# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/5/29.
"""

# 1. 外部不能访问函数内部变量
'''
def fun1():
    x = 1
print(x)
'''

# 2. 函数内部能访问函数外部变量
'''
x = 123
def fun2():
    print(x)

fun2()
'''


# 3. 函数里面不能修改外部变量
'''
x = 123
def func3():
    x = x + 1
    print(x)

func3()
'''

# 4. global修改全局变量
'''
x = 123
print(x)
def func2():
    global x
    x = x + 1
    print(x)

func2()
print(x)

'''
# 5.nonlocal让嵌套函数能够修改嵌套函数之外的值

def func4():
    b = 100
    # 没有被定义到func5
    def func5():
        print('-------')
        nonlocal b
        b += 1
        print(b)
    func5()
    print(b)
    # 运行func4所以才定义func5

func4()
