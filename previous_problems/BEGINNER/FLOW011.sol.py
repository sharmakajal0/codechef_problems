#!/usr/bin/env python
t = int(input())
for _ in range(t):
    n = int(input())
    if n < 1500:
        hra = n * 0.1
        da = n * 0.9
    else:
        hra = 500
        da = n * 0.98
    total = n + hra + da
    print(total)