#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b #print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

print(fib(6))

f = fib(5)
print('next(f):', next(f))
print('next(f):', next(f))
print('next(f):', next(f))
print('next(f):', next(f))
print('next(f):', next(f))
#print('next(f):', next(f)) #StopIteration: done

for n in fib(6):
    print(n)

#----------------------------------
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

o = odd()
next(o)
next(o)
next(o)
#next(o) #StopIteration

#----------------------------------
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator teturn value:', e.value)
        break

#----------------------------------
def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [L[i] + L[i+1] for i in range(len(L)-1)] + [1]

    pass

n=0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
'''
print out:
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
[1, 5, 10, 10, 5, 1]
[1, 6, 15, 20, 15, 6, 1]
[1, 7, 21, 35, 35, 21, 7, 1]
[1, 8, 28, 56, 70, 56, 28, 8, 1]
[1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
'''
