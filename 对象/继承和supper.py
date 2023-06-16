# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/6/6.
"""

class Father(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('这是老子')

    def __str__(self):
        return "%s的年龄是:%d" % (self.name, self.age)


class Son(Father):
    def __init__(self, name, age, collage):
        super().__init__(name, age)
        self.collage = collage
        print('---这是儿子要做的事---')

    def __str__(self):
        return "%s的年龄是:%d，他的学历是:%s" % (self.name, self.age, self.collage)


class GrandChild(Son):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("----这里模拟其要做的额外事情....----")


father = Father("父亲", 50)
print(father)

son = Son("儿子", 18, "大学")
print(son)

grandchild = GrandChild("孙子", 1, "未上学")
print(grandchild)