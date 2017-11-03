#!/usr/bin/env python
# -*- coding:utf-8 -*-

# lambda x: x* x
# 不用写return，返回值就是该表达式的结果

# 1.普通使用
l = list(map(lambda x: x* x, [1,2,3,4,5,6,7,8,9]))
print('l:',l)

# 2.作为函数对象赋值
f = lambda x: x * x

# 3.作为返回值返回
def build(x, y):
    return lambda: x * x + y * y

print(build(1,2)())