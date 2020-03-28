#!/usr/bin/env python
for _ in range(int(input())):
    x = int(input())
    n = 0
    if x % 10 == 0:
        n += 0
    elif x % 5 == 0 and x % 10 != 0:
        n += 1
    else:
        n -= 1
    print(n)
