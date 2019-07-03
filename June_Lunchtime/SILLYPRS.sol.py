#!/usr/bin/env python

def evenodd(l_1, l_2):
    Sum, even1, even2, odd1, odd2 = 0, 0, 0, 0, 0
    for i in l_1:
        Sum = Sum + i
        if i % 2 == 0:
            even1 += 1
        else:
            odd1 += 1
    for j in l_2:
        Sum = Sum + j
        if(j % 2 == 0):
            even2 += 1
        else:
            odd2 += 1
    Sum = Sum - abs(odd1 - odd2)
    return int(Sum/2)

T = int(input())

while T > 0:
    T = T - 1
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    print(evenodd(A, B))
