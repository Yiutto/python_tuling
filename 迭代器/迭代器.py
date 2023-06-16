# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/6/15.
"""

from collections.abc import Iterable, Iterator

print(isinstance('abc', Iterator))
print(isinstance('abc', Iterable))
print('*' * 20)
print(isinstance([1, 2, 3], Iterable))
print(isinstance([1, 2, 3], Iterator))
print('*' * 20)
print(isinstance(iter([1, 2, 3]), Iterable))
print(isinstance(iter([1, 2, 3]), Iterator))
print('*' * 20)
print(isinstance(1, Iterator))
print(isinstance(1, Iterable))
