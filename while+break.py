# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/5/24.
"""

db_user = 'yiutto'
db_pwd = '123456'

i = 0
while True:
    input_user = input("请输入用户名：")
    input_pwd = input("请输入用户密码：")
    if input_user == db_user and input_pwd == db_pwd:
        print("用户密码输入成功")
        print("登录成功")
        break  # 直接跳出循环
    else:
        print("用户名或密码错误")
        i += 1
        if i > 3:
            print("连续输入超过3次错误，请过5min再次登录")
            break