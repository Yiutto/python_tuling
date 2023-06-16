# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/6/7.
"""
class Tool:
    tools_num = 0  # 定义一个类属性，用来存储共享的数据

    def __init__(self, name):
        self.name = name
        Tool.tools_num += 1

    def print_info1(self):
        print(f'工具的总数为：{Tool.tools_num}')

    def print_info2():
        print(f"工具的总数为：{Tool.tools_num}")

tieqiao = Tool('铁锹')
chutou = Tool('锄头')

