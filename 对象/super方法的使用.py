# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/6/12.
"""

class Father:
    # 如果一个类中的方法的第一个参数是self， 那么这个方法就是一个实例方法
    # 实例方法必须使用实例对象
    def play_game(self):
        print('这是父类中的方法。。。。')

class Son(Father):
    # 重寫
    def play_game(self):
        # 通过父类名称.方法名在子类中调用
        # 如果在子类中调用父类的实例方法  那么需要传递一个实例对象
        Father.play_game(self)
        print('这是子类中的方法。。。')


        # 使用super方法在子类中调用父类方法
        super().play_game()
        print('这是。。。。')
s = Son()
s.play_game()


'''
super方法的主要功能：
    可以在子类中调用父类方法，并且不需要手动传递实例对象
'''