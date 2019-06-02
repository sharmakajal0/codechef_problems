#!/usr/bin/env python
#Python program for fibonacci sequence
def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    previous, current = 1, 1
    for i in range(n - 2):
        previous, current = current, previous + current

    return current

n = int(raw_input())

print fib(n)
