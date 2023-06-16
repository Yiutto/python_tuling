# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/5/29.
"""

# def func1(a, b, *c):
#     print(a)
#     print(b)
#     print(c)
#     print(*c)
#
# func1(1, 2, 3, 4, 5)
#
# # 报错
# # func1(1, 2, x=1, y=2)
#
# def func2(a, b, **c):
#     print(a)
#     print(b)
#     print(c)
#     print(*c)
#     #print(**c)
#
# # 报错
# #func2(1, 2, 3, 4)
# func2(1, 2, x=1, y=2)

# str1='HELLO'
# str2='我是来自火星的火星人'
# print(str1+','+str2)

# user = 'yiutto'
# pwd = '123456'
#
# input_user = input('请输入用户名：')
# input_pwd = input('请输入用户密码：')
#
# if input_user == user and input_pwd == pwd:
#     print('登录成功')
# else:
#     print('登录失败')
# i = 0
# while i < 10:
#     i += 1
#     if i in [3, 7, 8]:
#         continue
#     print(i)

# i = 0
# sum = 0
# while i <= 10:
#     sum += i
#     i += 1
# print(sum)
# i = 1
# while i < 11:
#     if i % 2 == 0:
#         print('%d为偶数' % i)
#     else:
#         print('%d为奇数' % i)
#     i += 1

# for i in range(0, 11):
#     if i % 2 == 0:
#         print('%d为偶数' % i)
#     else:
#         print('%d为奇数' % i)
#
# sb: bool = True

# info =[
#     {'name':'dahai','age':18},
#     {'name':'xialuo','age':78},
#     {'name':'xishi','age':8},
#     {'name':'dahai','age':18},
#     {'name':'dahai','age':18}
# ]
# L = []
# for i in info:
#     if i not in L:
#         L.append(i)
# print(L)
#
#
#
# c = 'dfssdf'
# print(c.__iter__().__next__())

# L = [i for i in range(1,101)]
# S = [L[i:i+3] for i in range(0,len(L), 3)]
# print(S)
#
# # 输出第1遍 佛祖镇楼
# print("                            _ooOoo_  ")
# print("                           o8888888o  ")
# print("                           88  .  88  ")
# print("                           (| -_- |)  ")
# print("                            O\\ = /O  ")
# print("                        ____/`---'\\____  ")
# print("                      .   ' \\| |// `.  ")
# print("                       / \\||| : |||// \\  ")
# print("                     / _||||| -:- |||||- \\  ")
# print("                       | | \\\\\\ - /// | |  ")
# print("                     | \\_| ''\\---/'' | |  ")
# print("                      \\ .-\\__ `-` ___/-. /  ")
# print("                   ___`. .' /--.--\\ `. . __  ")
# print("                ."" '< `.___\\_<|>_/___.' >'"".  ")
# print("               | | : `- \\`.;`\\ _ /`;.`/ - ` : | |  ")
# print("                 \\ \\ `-. \\_ __\\ /__ _/ .-` / /  ")
# print("         ======`-.____`-.___\\_____/___.-`____.-'======  ")
# print("                            `=---='  ")
# print("  ")
# print("         .............................................  ")
# print("                  佛祖镇楼                  BUG辟易  ")
# print("          佛曰:  ")
# print("                  写字楼里写字间，写字间里程序员；  ")
# print("                  程序人员写程序，又拿程序换酒钱。  ")
# print("                  酒醒只在网上坐，酒醉还来网下眠；  ")
# print("                  酒醉酒醒日复日，网上网下年复年。  ")
# print("                  但愿老死电脑间，不愿鞠躬老板前；  ")
# print("                  奔驰宝马贵者趣，公交自行程序员。  ")
# print("                  别人笑我忒疯癫，我笑自己命太贱；  ")
# print("                  不见满街漂亮妹，哪个归得程序员？")

# def getSum():
#     sum_int = 0
#     for i in range(1, 991):
#         sum_int += i
#     return sum_int
#
# sum_int = getSum()
# print(sum_int)
#
# def getSort(a, b, c):
#     L = [a, b, c]
#     L.sort()
#     print(L)
#
# getSort(1, 4, 3)
# getSort(3, 4, 1)
# getSort(4, 3, 1)
#
# def tranfer_rmb(a, b):
#     tranfer_dict = {
#         '美元': 6.84,
#         '欧元': 8.12,
#         '日元': 0.06,
#         '港元': 0.88,
#         '澳元': 4.98
#     }
#     print(f'金额为{b}{a}兑换的人民币为{tranfer_dict[a]*b}元')
#
# tranfer_rmb('美元', 100)
#
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def print_area(self):
#         print(f'矩形的面积为 {self.length * self.width} ')
#
#     def print_perimeter(self):
#         print(f'矩形的周长为 {2*(self.length+self.width)}')
#
# r = Rectangle(2, 4)
# r.print_area()
# r.print_perimeter()

# class Student:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def print_introduce(self):
#         print(f'我的名字叫{self.name}, 我的年龄{self.age}, 性别：{self.sex}')
#
# s = Student('yiutto', 29, 'man')
# s.print_introduce()


# class Parent:
#     x = 1
#
#
# class Child1(Parent):
#     pass
#
#
# class Child2(Parent):
#     pass
#
#
# print(Parent.x, Child1.x, Child2.x)   # 1,1,1
# Child1.x = 2
# print(Parent.x, Child1.x, Child2.x)   # 1,2,1
# Child1.x = 3
# print(Parent.x, Child1.x, Child2.x)   # 1,3,1
#
#
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def print_area(self):
#         print(f'矩形的面积为 {self.length * self.width} ')
#
# class Square(Rectangle):
#     def print_info(self):
#         if (self.width == self.length):
#             print(f'正方形的边长为{self.length}')
#         else:
#             print(f'该矩形不是正方形')
#
# s = Square(1, 2)
# s.print_info()
# s.print_area()
#
# t = Square(2, 2)
# t.print_info()
# t.print_area()
# 第三题
# 定义一个人们类作为父类，学生类继承这个人们类作为子类。
# 父类有一个__init__方法是可以生成对象的名字,年龄,性别属性，
# 子类（学生类）重写__init__方法，在重写的__init__方法里面，
# 子类（学生类）的__init__方法除了有父类的名字,年龄,性别的属性，
# 还有一个派生的属性:分数属性。实例化学生类，打印学生对象的姓名,年龄,性别,分数属性。

# class Person:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
# class Student(Person):
#     def __init__(self, name, age, gender, score):
#         self.score = score
#         super().__init__(name, age, gender)
#
# s = Student('yiutto', 28, '男', '99')
# print(s.name)
# print(s.age)
# print(s.gender)
# print(s.score)


obj_iter = [1,2,3,4,5,6,7,8,9]
obj_next=obj_iter.__iter__()
print(obj_next.__next__())
print(obj_next.__next__())
for i in obj_iter:
    print(i)

print('--------------------')
for i in obj_next:
    print(i)