# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/5/24.
"""

user = 'yiutto'
pwd = '123456'
balance = 10000
tag = True

while True:
    while tag:
        input_user = input("请输入用户名：")
        if input_user != user:
            print("输入用户名错误")
            continue
        else:
            input_pwd = input('请输入密码：')
            if input_pwd == pwd:
                print("登录成功")
                break
            else:
                print("输入密码错误")
    tag = False
    quqian = int(input('请输入取钱金额：'))
    if balance< quqian:
        print('余额不足，余额为：{}'.format(balance))
        print('请重新输入金额：')
    else:
        print('取钱成功，取走{}，还剩余{}'.format(quqian, balance-quqian))
        break

