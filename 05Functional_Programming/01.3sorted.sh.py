#!/usr/bin/env python
# -*- coding:utf-8 -*-

l = sorted([36, 5, -12, 9, -21])
print('l:', l)

l = sorted([36, 5, -12, 9, -21], key=abs)
print('l by abs:', l)