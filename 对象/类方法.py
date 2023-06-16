# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/6/13.
"""

'''
目前为止：
    实例方法  self
    静态方法   无
'''


class Father:
    @classmethod   #装饰器
    def print_info(cls):
        print('我是一个类方法')

'''
类方法中的第一个参数名称为cls
'''

class Tools:
    tool_num = 0  # 类属性

    def __init__(self, name):   # 构造方法
        self.name = name
        # 在实例化的过程对类属性自增1
        Tools.tool_num += 1

    # 实例方法
    def sum_tool_num1(self):
        # 类属性可以被类对象和实例对象访问
        print('工具总数为：', self.tool_num)
        print('工具总数为：', Tools.tool_num)

    # 类方法
    @classmethod
    def sum_tool_num2(cls):  # cls接收的是类对象：Tools类名
        print('工具总数为：', cls.tool_num)

tieqiao = Tools('铁锹')
chutou = Tools('锄头')
banshou = Tools('扳手')

# 多个实例对象可以同时访问类属性
print(tieqiao.tool_num)
print(chutou.tool_num)
print(banshou.tool_num)

tieqiao.sum_tool_num1()  # 实例方法
Tools.sum_tool_num2() # 类方法   改成实例方法调用也没问题


'''
1.类方法可以使用@classmethod 创建
2.类方法的第一个参数接收的是一个类对象

如果一个方法无需访问任何属性 可以使用静态方法 
如果一个方法需要访问一个类属性  那么可以使用类方法

省内存，提升代码复用性

'''