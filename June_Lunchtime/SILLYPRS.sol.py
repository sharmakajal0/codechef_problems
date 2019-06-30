#!/usr/bin/env python

from math import floor

def evenodd(l1, l2):
    S, even1, even2, odd1, odd2 = 0, 0, 0, 0, 0
    for i in l1:
        S = S + i
        if(i % 2 == 0):
            even1 += 1
        else:
            odd1 += 1
    for j in l2:
        S = S + j
        if(j % 2 == 0):
            even2 += 1
        else:
            odd2 += 1
    S = S - abs(odd1 - odd2)
    return int(S/2)   

T = int(input())

while T > 0:
    T = T - 1
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    print(evenodd(A, B))