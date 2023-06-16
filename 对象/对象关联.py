# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/6/7.
"""
'''
首先我使用的是班级类的实例对象输出的班级名称和学生名称

在班级类中动态创建一个属性，这个属性接收的是学生类的实例对象

通过在班级类中创建的属性用来接收学生类的实例对象之后则产生了关系
'''
class ClassRoom:
    def __init__(self, cls_name):
        self.cls_name = cls_name


class Student:
    def __init__(self, stu_name):
        self.stu_name = stu_name

# 把student1 集合到 python_cls1
python_cls1 = ClassRoom('python1班')
student1 = Student('anna')

# 如何给一个类动态创建属性
python_cls1.stu = student1

print(python_cls1.cls_name)
print(python_cls1.stu.stu_name)



class ClassRoom1:
    def __init__(self, cls_name):
        self.cls_name = cls_name
        self.student = None  # 默认设置为空

    def add_student(self, stu):
        self.student = stu

class Student1:
    def __init__(self, stu_name):
        self.stu_name = stu_name


cr1 = ClassRoom1('python二班')
std1 = Student1('yiutto')

cr1.add_student(std1)

print(cr1.student.stu_name)


class ClassRoom3:
    def __init__(self, cls_name):
        self.cls_name = cls_name
        self.stu_list = list()  # 添加多个对象

    def add_stu(self, stu):
        self.stu_list.append(stu)

class Student3:
    def __init__(self, stu_name):
        self.stu_name = stu_name

class_python3 = ClassRoom3('python三班')
py_std1 = Student3('yt')
py_std2 = Student3('lle')
class_python3.add_stu(py_std1)
class_python3.add_stu(py_std2)

for item in class_python3.stu_list:
    print(item.stu_name)