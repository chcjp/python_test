#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Decorator 装饰器， 一种高阶函数
def log(func):
    def wrapper(*arg, **kw):
        print('call %s' % func.__name__)
        func(*arg, **kw)
    return wrapper

#相当于 now = log(now)
@log
def now():
    print('2017-11-3')

f = now
f()
print(f.__name__) #本来是now，加了@log后变成wrapper

