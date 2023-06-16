# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/6/13.
"""

class Utils:
    tools_num = 3

    def __init__(self, name):
        self.name = name
        # 可以通过类名进行访问
        Utils.tools_num += 1
        # self.tools_num += 1
    @staticmethod
    def print_info():
        print('工具总数为：', Utils.tools_num)

tieqiao = Utils('铁锹')
tieqiao.print_info()
chutou = Utils('锄头')

print('工具总数', Utils.tools_num)
tieqiao.print_info()
'''
类属性类似与之前学习的局部变量
'''