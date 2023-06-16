# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/6/7.
"""
'''
子类中出现的方法名称如果和父类一样
    则子类会覆盖父类中的方法
    
重写：父类方法名与子类方法名必须保持一致

'''

class Father:
    def play_game(self):
        print('父类在play_game')

    def eat(self):
        print('父类在eat')


class Son(Father):
    def play_game(self):
        print('子类在play_game')


son = Son()
son.play_game()
son.eat()