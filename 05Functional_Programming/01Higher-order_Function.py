#/usr/bin/env python3
# -*- coding:utf-8 -*-

a = abs(-10)
print('a:', a) #a: 10
print(abs) #<built-in function abs>

f = abs #<built-in function abs>
x = f(-10) #10
print(f)
print('x:', x)

#函数名也是变量
#abs = 10
#abs(10) #TypeError: 'int' object is not callable

#abs函数实际上是定义在import builtins模块中的，所以要让修改abs变量的指向在其它模块也生效，
# 要用import builtins; builtins.abs = 10。

#高阶函数, 把函数作为参数传入
def add(x, y, f):
    return f(x) + f(y)

r = add(-5, 6, abs)
print('r:', r)
