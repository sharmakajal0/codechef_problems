#!usr/bin/env python
import math
t = int(input())
for _ in range(t):
    m, n = map(int, input().split())
    h = math.gcd(m, n)
    l = m*n/h
    print(h, int(l))