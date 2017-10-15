#/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
可以直接作用于for循环的数据类型有以下几种：

一类是集合数据类型，如list、tuple、dict、set、str等；

一类是generator，包括生成器和带yield的generator function。

这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。

可以使用isinstance()判断一个对象是否是Iterable对象：
'''

from collections import Iterable
from collections import Iterator

print('[]:', isinstance([], Iterable))
print('{}:', isinstance({}, Iterable))
print('abc:', isinstance('abc', Iterable))
print('(x for x in range(10)):', isinstance((x for x in range(10)), Iterable))
print('100:', isinstance(100, Iterable))

#Iterator 迭代器
print('Iterator []:', isinstance([], Iterator))
print('Iterator {}:', isinstance({}, Iterator))
print('Iterator "abc":', isinstance('abc', Iterator))

#list、dict、str等Iterable变成Iterator可以使用iter()函数：
print('Iterator iter([]):', isinstance(iter([]), Iterator))
print('Iterator iter("abc"):', isinstance(iter("abc"), Iterator))

#凡是可作用于for循环的对象都是Iterable类型；
#凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

