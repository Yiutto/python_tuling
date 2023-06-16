# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/6/4.
"""

def test(a, b, *args, **kwargs):
    print(f'{a}, {type(a)}')
    print(f'{b}, {type(b)}')
    # 如果形式参数已经接收到值之后还多除了一些其他的普通参数，则会被*args全部接收，并且类型为一个元组
    print(f'{args}, {type(args)}')
    print(f'{kwargs}, {type(kwargs)}')  # 默认参数的传递方式会被 **kwargs全部接收，并且打包成字典


test(1, 2, 3, 4, 5, 6, name='yiutto', age=30)

'''
*args  接收多出来的普通参数
**kwargs  接收多出来的命名参数（即关键字参数）

在使用*args 和 ** kwargs的时候，当前不定长参数位置必须声明在所有参数的后面！！


形式参数 > 默认参数 > args > kwargs
'''