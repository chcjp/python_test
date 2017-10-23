#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# filter() 过滤器，根据返回值是True 还是False 决定保留还是丢弃元素。
# filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。


def is_odd(n):
    return n % 2 == 1
l = list(filter(is_odd, [1,2,4,5,6,9,10,15]))
print('l:', l)


def not_empty(s):
    return s and s.strip()
l = list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
print('l:', l)


# 素数
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

print('primes: ')
for n in primes():
    if n < 1000:
        print(n)
    else:
        break

#练习:回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数：
def is_palindrome(n):
    num = str(n)
    pass

# 测试:
output = filter(is_palindrome, range(1, 1000))
print(list(output))