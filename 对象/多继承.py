# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/6/7.
"""
class A:
    pass
class B:
    pass
class C(A, B):
    pass

'''
使用一个子类继承多个父类
    当前这个子类可以获取多个父类的方法和属性
'''

class Camera:
    def take_photo(self):
        print('拍照')


class Game:
    def play_game(self):
        print('玩游戏')


class Phone(Camera, Game):
    def call(self):
        print('打电话')


phone = Phone()
phone.call()
phone.play_game()
phone.take_photo()