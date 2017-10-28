#!/usr/bin/env python
# -*- coding:utf-8 -*-

#1. 函数作为返回值
# 普通函数
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

#返回函数的函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1,3,5,7,9)
print('f:', f)
print('f():', f()) #调用f,才真正求和

f2 = lazy_sum(1,3,5,7,9)
print('f==f2:', f==f2)#每次调用都会生成一个新函数

#2. 闭包
def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1,f2,f3 = count()
print('f1():', f1)# <function count.<locals>.f at 0x005BC8E8>
print('f1():', f1())# 9
print('f2():', f2())# 9
print('f3():', f3())# 9

#改进版本
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1,f2,f3 = count()
print('new f1():', f1())# 1
print('new f2():', f2())# 4
print('new f3():', f3())# 9