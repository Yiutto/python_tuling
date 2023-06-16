# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/6/15.
"""

class StudentSystem:

    # 构造函数
    def __init__(self):
        self.stu_list = []
        # 计数器
        self.current = 0

    def add_student(self):
        name = input('请输入学生姓名：')
        tel = input('请输入学生手机号：')
        address = input('请输入学生地址：')

        new_stu_dict = {
            'name': name,
            'tel': tel,
            'address': address
        }
        self.stu_list.append(new_stu_dict)

    # 迭代对象  当前类自身就是一个迭代器，返回本身实例即可
    def __iter__(self):
        return self

    def __next__(self):
        if self.current < len(self.stu_list):
            res = self.stu_list[self.current]
            self.current += 1
            return res
        else:
            raise StopIteration

# 创建实例对象
stu_obj = StudentSystem()

for _ in range(3):
    stu_obj.add_student()


for item in stu_obj:
    print(item)

'''
如果要让一个类成为迭代对象
     __iter__
     
如果要让一个类成本迭代器对象
    __next__
    
如果__iter__和__next__方法在一个类中
return self
return res
'''