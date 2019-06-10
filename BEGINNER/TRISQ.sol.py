#!/usr/bin/env python
t = int(input())
for _ in range(t):
    B = int(input())
    def square(B):
        B = B-2
        B = int(B/2)
        C = (B + 1)/2
        D = int(B * C)
        return D
    print(square(B))