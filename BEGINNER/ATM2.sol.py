#!/usr/bin/env python
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    P = []
    A = list(map(int, input().strip().split(' ')))
    for i in A:
        if k >= i:
            k = k - i
            P.append("1")
        else:
            P.append("0")
    for i in range(n):
        print(P[i], end = '')
    print("\n")