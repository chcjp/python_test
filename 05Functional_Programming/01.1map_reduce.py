#/usr/bin/env python3
# -*- coding:utf-8 -*-

# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

def f(x):
    return x * x

r = map(f, range(1,10))
l = list(r)
#print('r:', next(r)) #StopIteration ?
print('l:', l)

#不推荐做法
L = []
for n in range(1,10):
    L.append(f(n))
print('L:', L)

s = list(map(str, [1,2,3,4,5,6,7,8,9]))
print('s:', s)

# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce
def add(x, y):
    return x + y

s = reduce(add, [1, 3, 5, 7, 9])
print('sum:', s)

a = sum([1, 3, 5, 7, 9])
print('sum2:', a)


# ----------------------------------------

def fn(x, y):
    return x * 10 + y

num = reduce(fn, [1,3,5,7,9])
print('num:', num)

def char2num(s):
    return {'0':0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

str2num = reduce(fn, map(char2num, '13579'))
print('str2num:', str2num)

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0':0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))

num2 = str2int('24680')
print('num2:', num2)
