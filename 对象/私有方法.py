# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/6/7.
"""

class BankService:

    # 私有属性的使用以及创建就可以
    def __bank_to_bank(self, money):
        return f'模拟转账代码...:{money}'

    def info(self):
        money = int(input('请输入转账金额：'))
        if money>=200:
            print(self.__bank_to_bank(money))
        else:
            print('钱不够，留着自己吃屎')

bs = BankService()
print(bs.info())
print(bs._BankService__bank_to_bank(100))
