#!/usr/bin/env python
# -*- coding:utf-8 -*-

l = sorted([36, 5, -12, 9, -21])
print('l:', l)

l = sorted([36, 5, -12, 9, -21], key=abs)
print('l by abs:', l)

l = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print('str l:', l)

# reverse sorted
l = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
print('str l2:', l)

# practice
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return str.lower(t[0])
    pass
L2 = sorted(L, key=by_name)
print('L2:', L2)

def by_score(t):
    return t[1]
    pass

L2 = sorted(L, key=by_score, reverse=True)
print('L2 by score:', L2)