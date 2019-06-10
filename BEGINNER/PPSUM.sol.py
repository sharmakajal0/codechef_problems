#!/usr/bin/env python
t = int(input())
for _ in range(1, t + 1):
    n,d = map(int, input().split())
    for _ in range(1, n + 1):
        d = (d * (d + 1)) // 2
        n = n - 1
    print(d)